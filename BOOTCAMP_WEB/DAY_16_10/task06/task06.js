const campos = {
    type: document.getElementById('type'),
    brand: document.getElementById('brand'),
    price: document.getElementById('price'),
    number: document.getElementById('number')
};
const botao = document.getElementById('salvar');
const divAlerta = document.getElementById('alerta');

function mostrarAlerta(mensagem, tipo) {
    divAlerta.innerHTML = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${mensagem}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
}

botao.addEventListener('click', async () => {
    const parametros = new URLSearchParams({
        type: campos.type.value,
        brand: campos.brand.value,
        price: campos.price.value,
        number: campos.number.value
    });

    try {
        const resposta = await fetch('task06.php?' + parametros);
        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(dados.error ?? 'status ' + resposta.status);
        }
        mostrarAlerta(dados.message, 'success');
    } catch (erro) {
        mostrarAlerta(erro.message, 'danger');
    }
});
