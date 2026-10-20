<?php

header('Content-Type: application/json');

$email = $_POST['email'] ?? '';

if (filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
    http_response_code(400);
    echo json_encode(['valid' => false, 'message' => "$email is not a valid email address."]);
    return;
}

echo json_encode(['valid' => true, 'message' => "$email is a valid email address."]);
