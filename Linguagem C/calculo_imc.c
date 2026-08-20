#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese_Brazil");
    float peso, altura, imc;
    printf("Digite o seu peso: ");
    scanf("%f", &peso);
    printf("Digite a sua altura: ");
    scanf("%f", &altura);
    imc = peso / (altura * altura);
    //Estrutura Consdicional Encadeada (if - else if - else)
    if(imc <= 18.5){
             printf("IMC: %.2f - Magreza.\n", imc);
    } else if(imc <= 24.9){
          printf("IMC: %.2f - Normal.\n", imc);
    } else if(imc <= 29.9){
          printf("IMC: %.2f - Sobrepeso.\n", imc);
    } else if(imc <= 39.9){
          printf("IMC: %.2f - Obesidade.\n", imc);
    } else {
          printf("IMC: %.2f - Obesidade grave.\n", imc);
    }
    
    system("pause");
    return 0;
}
