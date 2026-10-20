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

function check_brand(string $brand): ?string
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
    return null;
}

// O preço aceita o operador da task05 para reaproveitar o mesmo campo; só o número é gravado.
function check_price(string $price): ?string
{
    if ($price === '') {
        return "Error ($price): this price does not have enough characters.";
    }
    if (strlen($price) > 5) {
        return "Error ($price): this price has too many characters.";
    }
    if (!preg_match('/^[<>=]?[0-9]+$/', $price)) {
        return "Error ($price): we cannot define a price - string invalid.";
    }
    return null;
}

function check_number(string $number): ?string
{
    if (!preg_match('/^[0-9]+$/', $number)) {
        return "Error ($number): not a positive number.";
    }
    return null;
}

function price_value(string $price): int
{
    return (int) ltrim($price, '<>=');
}

function save(PDO $pdo, string $type, string $brand, int $price, int $stock): string
{
    $query = $pdo->prepare('SELECT id FROM products WHERE type = ? COLLATE NOCASE AND brand = ? COLLATE NOCASE');
    $query->execute([$type, $brand]);
    $id = $query->fetchColumn();

    if ($id === false) {
        $pdo->prepare('INSERT INTO products (type, brand, price, stock) VALUES (?, ?, ?, ?)')
            ->execute([$type, $brand, $price, $stock]);
        return "$brand ($type) was added with price $price and stock $stock.";
    }

    $pdo->prepare('UPDATE products SET price = ?, stock = ? WHERE id = ?')
        ->execute([$price, $stock, $id]);
    return "$brand ($type) already existed: price updated to $price and stock to $stock.";
}

function handle_request(): void
{
    header('Content-Type: application/json');

    $type = $_GET['type'] ?? '';
    $brand = $_GET['brand'] ?? '';
    $price = $_GET['price'] ?? '';
    $number = $_GET['number'] ?? '';

    try {
        $pdo = db();

        $erro = check_type($pdo, $type)
            ?? check_brand($brand)
            ?? check_price($price)
            ?? check_number($number);
        if ($erro !== null) {
            http_response_code(400);
            echo json_encode(['error' => $erro]);
            return;
        }

        $mensagem = save($pdo, $type, $brand, price_value($price), (int) $number);
        echo json_encode(['message' => $mensagem]);
    } catch (PDOException $erro) {
        http_response_code(500);
        echo json_encode(['error' => 'database error: ' . $erro->getMessage()]);
    }
}

if (PHP_SAPI !== 'cli') {
    handle_request();
}
