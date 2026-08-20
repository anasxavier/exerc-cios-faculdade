#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese_Brazil");
	//Declarar as variáveis
	char produto[50]; //caracter
	int unidades; //número inteiro
	float valor; //números reais
	
	printf("===== Loja do seu Zé =====\n");
	//printf => saida de dados
	printf("Digite o nome do produto: ");
	//Entrada de dados => scanf / fgets
	fgets(produto, 50, stdin);
	printf("Digite a quantidade em unidades: ");
	scanf("%d", &unidades);// "%d" ativar o int "&" para gravar a variavel
	printf("Digite o valor por unidade: R$");
	scanf("%f", &valor);// "%f" ativar o flat "&" para gravar a variavel
	printf("===== Relatório de Produtos =====\n");
	printf("Produto: \t%s\n", produto);// "\t" alinhamento "%s" ativar o char e "\n" quebra de linha
	printf("Unidades: \t%d\n", unidades);// "\t" alinhamento "%s" ativar o int e "\n" quebra de linha
	printf("Valor: \t\tR$%.2f\n", valor);
	
	system("pause");
	return 0; 
}
