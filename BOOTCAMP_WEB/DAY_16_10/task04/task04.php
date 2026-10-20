<?php

function db(): PDO
{
    $pdo = new PDO('sqlite:' . __DIR__ . '/ajax_products.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    return $pdo;
}

function check_type(PDO $pdo, string $type): array
{
    if ($type === '') {
        return [false, 'No type sent yet!'];
    }
    if (strlen($type) < 3) {
        return [false, "$type: this type does not have enough characters."];
    }
    if (strlen($type) > 10) {
        return [false, "$type: this type has too many characters."];
    }
    if (!preg_match('/^[a-z-]+$/i', $type)) {
        return [false, "$type: this type has non-alphabetical characters (different from '-')."];
    }

    $query = $pdo->prepare('SELECT 1 FROM products WHERE type = ? COLLATE NOCASE LIMIT 1');
    $query->execute([$type]);
    if ($query->fetchColumn() === false) {
        return [false, "$type: this type doesn't exist in our shop."];
    }
    return [true, "$type: this type exists in databases."];
}

// shortcut: a marca é procurada em toda a tabela, não no par (type, brand) — trocar por
// uma busca no par se a loja passar a aceitar a mesma marca em tipos diferentes.
function check_brand(PDO $pdo, string $brand, string $type, bool $type_ok): array
{
    if ($brand === '') {
        return [false, 'No brand sent yet!'];
    }
    if (strlen($brand) < 2) {
        return [false, "$brand: this brand does not have enough characters."];
    }
    if (strlen($brand) > 20) {
        return [false, "$brand: this brand has too many characters."];
    }
    if (!preg_match('/^[a-z0-9&-]+$/i', $brand)) {
        return [false, "$brand: this brand has invalid characters."];
    }

    $query = $pdo->prepare('SELECT 1 FROM products WHERE brand = ? COLLATE NOCASE LIMIT 1');
    $query->execute([$brand]);
    if ($query->fetchColumn() !== false) {
        return [false, "$brand: this brand already exists in databases."];
    }
    return [$type_ok, "$brand: this brand is valid for the type $type."];
}

header('Content-Type: application/json');

$type = $_GET['type'] ?? '';
$brand = $_GET['brand'] ?? '';

try {
    $pdo = db();
    [$type_ok, $type_message] = check_type($pdo, $type);
    [$brand_ok, $brand_message] = check_brand($pdo, $brand, $type, $type_ok);

    echo json_encode([
        'type' => ['valid' => $type_ok, 'message' => $type_message],
        'brand' => ['valid' => $brand_ok, 'message' => $brand_message],
    ]);
} catch (PDOException $erro) {
    http_response_code(500);
    echo json_encode(['error' => 'database error: ' . $erro->getMessage()]);
}
