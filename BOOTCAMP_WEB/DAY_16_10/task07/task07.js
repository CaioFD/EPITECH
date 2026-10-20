const formulario = document.getElementById('formulario');
const campoNome = document.getElementById('nome');
const campoMensagem = document.getElementById('mensagem');
const lista = document.getElementById('mensagens');
const divAlerta = document.getElementById('alerta');

function mostrarAlerta(mensagem, tipo) {
    divAlerta.innerHTML = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${mensagem}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
}

// textContent em vez de innerHTML: a mensagem vem de outro usuário.
function desenhar(mensagens) {
    lista.innerHTML = '';

    for (const item of mensagens) {
        const linha = document.createElement('li');
        linha.className = 'list-group-item';

        const autor = document.createElement('strong');
        autor.textContent = `${item.name} (${item.time}): `;
        linha.append(autor, document.createTextNode(item.message));

        lista.append(linha);
    }
    lista.scrollTop = lista.scrollHeight;
}

async function carregar(opcoes = {}) {
    try {
        const resposta = await fetch('task07.php', opcoes);
        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(dados.error ?? 'status ' + resposta.status);
        }
        desenhar(dados.messages);
    } catch (erro) {
        mostrarAlerta('Ocorreu um erro: ' + erro.message, 'danger');
    }
}

formulario.addEventListener('submit', async (evento) => {
    evento.preventDefault();

    await carregar({ method: 'POST', body: new URLSearchParams(new FormData(formulario)) });
    campoMensagem.value = '';
});

carregar();
setInterval(carregar, 4000);
