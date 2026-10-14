<?php
 
function calc_average(array $numbers)
{
    if (count($numbers) === 0) {
        return 0.0;
    }
    return round(array_sum($numbers) / count($numbers), 1);
}