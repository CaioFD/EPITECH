<?php
 
function form_is_submitted()
{
    return isset($_POST["submit"]);
}
 
function whoami()
{
    $name = isset($_POST["name"]) && $_POST["name"] !== "" ? $_POST["name"] : null;
    $age = isset($_POST["age"]) && ctype_digit($_POST["age"]) ? $_POST["age"] : null;
 
    if ($name !== null && $age !== null) {
        echo "Hi, my name is $name and I'm $age years old.";
    } elseif ($name === null && $age !== null) {
        echo "Hi, I have no name and I'm $age years old.";
    } elseif ($name !== null) {
        echo "Hi, my name is $name.";
    } else {
        echo "Hi, I have no name.";
    }
 
    $curriculums = [
        "pge" => "PGE",
        "bachelor" => "Bachelor",
        "msc" => "MSC Pro",
        "coding" => "Coding Academy",
        "wac" => "Web@cademie",
    ];
    if (isset($_POST["curriculum"]) && isset($curriculums[$_POST["curriculum"]])) {
        echo " I'm a student of " . $curriculums[$_POST["curriculum"]] . ".";
    }
}