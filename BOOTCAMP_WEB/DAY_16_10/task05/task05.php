<?php

function db(): PDO
{
    $pdo = new PDO('sqlite:' . __DIR__ . '/ajax_products.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    return $pdo;
}

function check_type(PDO $pdo, string $type): ?string
{
    if (strlen($type) < 3) {
        return "Error ($type): this type does not have enough characters.";
    }
    if (strlen($type) > 10) {
        return "Error ($type): this type has too many characters.";
    }
    if (!preg_match('/^[a-z-]+$/i', $type)) {
        return "Error ($type): this type has non-alphabetical characters (different from '-').";
    }

    $query = $pdo->prepare('SELECT 1 FROM products WHERE type = ? COLLATE NOCASE LIMIT 1');
    $query->execute([$type]);
    if ($query->fetchColumn() === false) {
        return "Error ($type): this type doesn't exist in our shop.";
    }
    return null;
}

function check_brand(PDO $pdo, string $brand, string $type): ?string
{
    if (strlen($brand) < 2) {
        return "Error ($brand): this brand does not have enough characters.";
    }
    if (strlen($brand) > 20) {
        return "Error ($brand): this brand has too much characters.";
    }
    if (!preg_match('/^[a-z0-9&-]+$/i', $brand)) {
        return "Error ($brand): this brand has invalid characters.";
    }

    $query = $pdo->prepare('SELECT 1 FROM products WHERE type = ? COLLATE NOCASE AND brand = ? COLLATE NOCASE LIMIT 1');
    $query->execute([$type, $brand]);
    if ($query->fetchColumn() === false) {
        return "Error ($brand): this brand doesn't exist in our database.";
    }
    return null;
}

function check_price(string $price): ?string
{
    if (strlen($price) < 2) {
        return "Error ($price): this price does not have enough characters.";
    }
    if (strlen($price) > 5) {
        return "Error ($price): this price has too many characters.";
    }
    if (!preg_match('/^[<>=][0-9]+$/', $price)) {
        return "Error ($price): we cannot define a price - string invalid.";
    }
    return null;
}

function search(PDO $pdo, string $type, string $brand, string $price): array
{
    $operator = $price[0];
    $value = (int) substr($price, 1);

    $query = $pdo->prepare(
        "SELECT type, brand, price, stock FROM products
         WHERE type = ? COLLATE NOCASE AND brand = ? COLLATE NOCASE AND price $operator ?"
    );
    $query->execute([$type, $brand, $value]);
    return $query->fetchAll(PDO::FETCH_ASSOC);
}

function fail(string $message): void
{
    http_response_code(400);
    echo json_encode(['error' => $message]);
}

header('Content-Type: application/json');

$type = $_GET['type'] ?? '';
$brand = $_GET['brand'] ?? '';
$price = $_GET['price'] ?? '';
$number = $_GET['number'] ?? '';

try {
    $pdo = db();

    $erro = check_type($pdo, $type)
        ?? check_brand($pdo, $brand, $type)
        ?? check_price($price);
    if ($erro !== null) {
        fail($erro);
        return;
    }

    $produtos = search($pdo, $type, $brand, $price);
    if ($produtos === []) {
        fail("Error ($price): no products found at this price.");
        return;
    }

    if (!preg_match('/^[0-9]+$/', $number) || (int) $number <= 0) {
        fail("Error ($number): not a positive number.");
        return;
    }

    $wanted = (int) $number;
    $disponiveis = array_values(array_filter($produtos, fn ($p) => $p['stock'] >= $wanted));
    if ($disponiveis === []) {
        $stock = max(array_column($produtos, 'stock'));
        fail("Error ($number): sorry, we don't have enough stock, we only have $stock in stock.");
        return;
    }

    foreach ($disponiveis as &$produto) {
        $produto['number'] = $wanted;
    }
    echo json_encode(['products' => $disponiveis]);
} catch (PDOException $erro) {
    http_response_code(500);
    echo json_encode(['error' => 'database error: ' . $erro->getMessage()]);
}
