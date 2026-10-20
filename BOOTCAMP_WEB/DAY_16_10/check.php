<?php
// Self-check das validações (CLI): php check.php
require __DIR__ . '/task06/task06.php';

$pdo = db();
$casos = [
    [check_type($pdo, 'tv'), "Error (tv): this type does not have enough characters."],
    [check_type($pdo, 'abcdefghijk'), "Error (abcdefghijk): this type has too many characters."],
    [check_type($pdo, 'lap1op'), "Error (lap1op): this type has non-alphabetical characters (different from '-')."],
    [check_type($pdo, 'banana'), "Error (banana): this type doesn't exist in our shop."],
    [check_type($pdo, 'LAPTOP'), null],
    [check_brand('A'), "Error (A): this brand does not have enough characters."],
    [check_brand('Nike!'), "Error (Nike!): this brand has invalid characters."],
    [check_brand('H&M-2'), null],
    [check_price(''), "Error (): this price does not have enough characters."],
    [check_price('>12345'), "Error (>12345): this price has too many characters."],
    [check_price('abc'), "Error (abc): we cannot define a price - string invalid."],
    [check_price('>100'), null],
    [check_number('-1'), "Error (-1): not a positive number."],
    [check_number('0'), null],
    [price_value('>100'), 100],
    [price_value('42'), 42],
];

$falhas = 0;
foreach ($casos as $i => [$obtido, $esperado]) {
    if ($obtido !== $esperado) {
        $falhas++;
        echo "FAIL #$i: got " . var_export($obtido, true) . ", want " . var_export($esperado, true) . "\n";
    }
}
echo $falhas === 0 ? "all " . count($casos) . " checks passed\n" : "$falhas failure(s)\n";
