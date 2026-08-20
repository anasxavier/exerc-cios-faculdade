#include<stdio.h>
#include<stdlib.h> 
#include<locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese_Brazil");
    //while
    float nota1, nota2, nota3, media;
    int sair;
    sair = 1;
    do{
      
        printf("Digite nota 01: ");
        scanf("%f", &nota1);
        printf("Digite nota 02: ");
        scanf("%f", &nota2);
        printf("Digite nota 03: ");
        scanf("%f", &nota3);
        //calculo
        media = (nota1 + nota2 + nota3) /3;
        
        printf("Sua média final é %.2f\n", media);
        printf("Deseja calcular outra média? [1] Sim [2] Não\n");
        scanf("%d", &sair);   
    }while(sair == 1);
    
    system("pause");
    return 0;
}
