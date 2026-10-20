const campoType = document.getElementById('type');
const campoBrand = document.getElementById('brand');
const msgType = document.getElementById('msg-type');
const msgBrand = document.getElementById('msg-brand');

function mostrar(elemento, resultado) {
    elemento.textContent = resultado.message;
    elemento.className = resultado.valid ? 'text-success' : 'text-danger';
}

async function validar() {
    const parametros = new URLSearchParams({
        type: campoType.value,
        brand: campoBrand.value
    });

    try {
        const resposta = await fetch('task04.php?' + parametros);
        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(dados.error ?? 'status ' + resposta.status);
        }

        mostrar(msgType, dados.type);
        mostrar(msgBrand, dados.brand);
    } catch (erro) {
        mostrar(msgType, { valid: false, message: 'Ocorreu um erro: ' + erro.message });
        msgBrand.textContent = '';
    }
}

campoType.addEventListener('input', validar);
campoBrand.addEventListener('input', validar);
validar();
