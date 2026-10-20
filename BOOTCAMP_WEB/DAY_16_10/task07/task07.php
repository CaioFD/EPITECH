<?php

const ARQUIVO = __DIR__ . '/messages.json';
const LIMITE = 50;

function read_messages(): array
{
    if (!file_exists(ARQUIVO)) {
        return [];
    }
    return json_decode(file_get_contents(ARQUIVO), true) ?? [];
}

function add_message(string $name, string $message): void
{
    $arquivo = fopen(ARQUIVO, 'c+');
    flock($arquivo, LOCK_EX);

    $conteudo = stream_get_contents($arquivo);
    $mensagens = json_decode($conteudo, true) ?? [];
    $mensagens[] = ['name' => $name, 'message' => $message, 'time' => date('H:i:s')];
    $mensagens = array_slice($mensagens, -LIMITE);

    ftruncate($arquivo, 0);
    rewind($arquivo);
    fwrite($arquivo, json_encode($mensagens));

    flock($arquivo, LOCK_UN);
    fclose($arquivo);
}

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['messages' => read_messages()]);
    return;
}

$name = trim($_POST['name'] ?? '');
$message = trim($_POST['message'] ?? '');

if ($name === '' || $message === '') {
    http_response_code(400);
    echo json_encode(['error' => 'Name and message are required.']);
    return;
}
if (strlen($name) > 30 || strlen($message) > 500) {
    http_response_code(400);
    echo json_encode(['error' => 'Name (30) or message (500) is too long.']);
    return;
}

add_message($name, $message);
echo json_encode(['messages' => read_messages()]);
