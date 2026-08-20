#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese_Brazil");
    int idade;
    idade = 10;
    //Estrutura Consdicional Encadeada (if - else if - else)
    if(idade < 12) {
             printf("Enrada Proibida\n");
    } else if(idade < 18) {
           printf("Entrada permitida se acompanhada dos pais\n");
    }else {
          printf("Enrada permitida\n");
    }
    
    
    system("pause");
    return 0;
}
