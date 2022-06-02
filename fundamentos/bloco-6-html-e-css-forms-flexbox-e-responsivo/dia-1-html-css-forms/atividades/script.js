const button = document.querySelector("#submit");
let nome= document.querySelector("#Nome");

function parar(event){
    // event.preventDefault();
    console.log(nome.value)
};

button.addEventListener('click', parar);