<?php
 
function get_shortest(array $strings)
{
    $shortest = null;
    foreach ($strings as $str) {
        if ($shortest === null || strlen($str) < strlen($shortest)) {
            $shortest = $str;
        }
    }
    return $shortest;
}