<?php
 
function calc(string $operator, int $nbr1, int $nbr2)
{
    if (!in_array($operator, ["+", "-", "*", "/", "%"], true)) {
        return "Unknown operator";
    }
    if (($operator === "/" || $operator === "%") && $nbr2 === 0) {
        return "Cannot divide by 0";
    }
    switch ($operator) {
        case "+": return $nbr1 + $nbr2;
        case "-": return $nbr1 - $nbr2;
        case "*": return $nbr1 * $nbr2;
        case "/": return $nbr1 / $nbr2;
        case "%": return $nbr1 % $nbr2;
    }
}