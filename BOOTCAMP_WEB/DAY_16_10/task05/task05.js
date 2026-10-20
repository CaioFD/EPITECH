const campos = {
    type: document.getElementById('type'),
    brand: document.getElementById('brand'),
    price: document.getElementById('price'),
    number: document.getElementById('number')
};
const botao = document.getElementById('buscar');
const divAlerta = document.getElementById('alerta');
const corpo = document.getElementById('corpo');

function mostrarAlerta(mensagem, tipo) {
    divAlerta.innerHTML = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${mensagem}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
}

botao.addEventListener('click', async () => {
    corpo.innerHTML = '';
    divAlerta.innerHTML = '';

    const parametros = new URLSearchParams({
        type: campos.type.value,
        brand: campos.brand.value,
        price: campos.price.value,
        number: campos.number.value
    });

    try {
        const resposta = await fetch('task05.php?' + parametros);
        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(dados.error ?? 'status ' + resposta.status);
        }

        for (const produto of dados.products) {
            const linha = corpo.insertRow();
            for (const chave of ['type', 'brand', 'price', 'number', 'stock']) {
                linha.insertCell().textContent = produto[chave];
            }
        }
        mostrarAlerta(`${dados.products.length} produto(s) encontrado(s).`, 'success');
    } catch (erro) {
        mostrarAlerta(erro.message, 'danger');
    }
});
