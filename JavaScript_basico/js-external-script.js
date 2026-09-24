var idade = prompt("Digite sua idade")
idade = parseInt(idade)

if (idade > 18){
    document.write("Idade Maior que 18")
} else if (idade == 18) {
    document.write("Idade Igual a 18")
} else {
    document.write("Idade Menor que 18")
}