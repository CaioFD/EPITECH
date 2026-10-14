<?php
 
function dog_bark(int $woof_nb)
{
    $woofs = array_fill(0, max($woof_nb, 0), "woof");
    echo implode(" ", $woofs) . PHP_EOL;
}
 