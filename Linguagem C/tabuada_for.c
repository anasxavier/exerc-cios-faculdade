#include<stdio.h>
#include<stdlib.h> 
#include<locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese_Brazil");
    int numero, i;
    
    for(i = 0; i <= 10; i ++){
          numero = i * 6;
          printf("6 * %d = %d\n", i, numero);
    }
     for(i = 1; i <= 10; i ++){
          printf("%d\n", i);
     }
     
     
    system("pause");
    return 0;
}
