#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

int main (){
    setlocale(LC_ALL, "Portuguese_Brazil");
    //Variáveis
    int tipoCombustivel;
    float litros, valorGasolina, valorEtanol, valorTotal, valorDesconto;
    valorGasolina = 6.90;
    valorEtanol = 4.90;
    
    printf("====Posto do seu Zé=====\n");
    
    printf("Escolha o combustível abastecido:\n");
    printf("[1] - Gasolina\n[2] - Etanol\n");
    printf("R: ");
    scanf("%d", &tipoCombustivel);
    printf("Quantos litros foram abastecido: ");
    scanf("%f", litros);
    
    switch(tipoCombustivel){     
         case 1:
              if(litros > 25){
                     valorTotal = litros * valorGasolina;
                     valorDesconto = valorTotal - (valorTotal * 0.09);
              } 
              else{
                 valorTotal = litros * valorGasolina;
                 valorDesconto = valorTotal - (valorTotal * 0.07);     
              }
          break;
          case 2:
            if(litros > 25){
                     valorTotal = litros * valorEtanol;
                     valorDesconto = valorTotal - (valorTotal * 0.075);
              } 
              else{
                 valorTotal = litros * valorEtanol;
                 valorDesconto = valorTotal - (valorTotal * 0.05);
              }      
            break;
            default:
                    printf("[Erro] - Combutível Inválido\n");
                    return 0;
    }
    
    printf("===== Resumo =====\n");
    printf("Valor Total: R$ %.2f\nValor com Desconto: R$ %.2f\n", valorTotal, valorDesconto);
        
    system ("pause");
    return 0;
}
