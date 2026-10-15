<?php
 
function dynamic_body()
{
    $page = $_GET["page"] ?? "";
    if (!in_array($page, ["home", "php", "sql"], true)) {
        return "<p>Unknown page</p>";
    }
    return file_get_contents($page . ".html");
}