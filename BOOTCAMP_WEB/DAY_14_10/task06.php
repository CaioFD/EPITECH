<?php
 
function sequence(int $n): void
{
    if ($n < 0) {
        return;
    }
    $current = "1";
    for ($i = 0; $i <= $n; $i++) {
        echo $current . PHP_EOL;
        $next = "";
        $len = strlen($current);
        for ($j = 0; $j < $len; ) {
            $k = $j;
            while ($k < $len && $current[$k] === $current[$j]) {
                $k++;
            }
            $next .= ($k - $j) . $current[$j];
            $j = $k;
        }
        $current = $next;
    }
}
