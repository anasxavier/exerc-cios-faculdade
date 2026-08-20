#include<stdio.h>
#include<stdlib.h> 
#include<locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese_Brazil");
    int chute, correto;
    correto = 10;
    
    while(chute != correto){
         printf("Digite o seu chute: ");
         scanf("%d", &chute);
         if(chute < correto){
                  printf("Muito baixo. Tente novamente novamente!");
         }else if(chute > correto){
               printf("Muito alto. Tente novamente!");
         }else  {
                  printf("Parabéns!! Você acertou o número secreto");
         }
    }
    
    system("pause");
    return 0;
}
