const botao = document.querySelector("button");


const lista = document.querySelector("ul");

botao.addEventListener("click", function() {

    const textoInserido = document.querySelector("input").value;

    const resultado = document.createElement("li");
    const texto = document.createTextNode(parseInt(textoInserido) ** 2);
    resultado.appendChild(texto);
    lista.appendChild(resultado);

})


