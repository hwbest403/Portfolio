/*#include <stdio.h>
#include <stdlib.h>

void std(char* stdname, int* stdnum);
void PrintResult(int a, int b, int option, float result, char* stdname, int stdnum);
int getOption(void);
void getdata(int* a, int* b);
float calc(int option, int a, int b);
float add(int a, int b);
float subtract(int a, int b);
float multiply(int a, int b);
float quotient(int a, int b);

void main()
{
	int option;
	char stdname[10];
	int stdnum;
	int a;
	int b;
	float result;

	std(stdname, &stdnum);
	option = getOption();
	getdata(&a, &b);
	result = calc(option, a, b);
	PrintResult(a, b, option, result, stdname, stdnum);

	return;

}

void std(char* stdname, int* stdnum)
{
	printf("성명:");
	scanf("%s", stdname);
	printf("학번:");
	scanf("%d", stdnum);
	return;
}

int getOption(void)
{
	int option1;
	int option;

	printf("\t*****************************");
	printf("\n\t*           MENU            *");
	printf("\n\t*  1. ADD                   *");
	printf("\n\t*  2. SUBTRACT              *");
	printf("\n\t*  3. MULTIPLY              *");
	printf("\n\t*  4. DIVIDE                *");
	printf("\n\t*                           *");
	printf("\n\t*****************************");

	printf("\n\nPlease type your choice ");
	printf("and key return: ");
	scanf("%d", &option1);
	switch (option1)
	{
	case 1: option = option1;
		break;
	case 2: option = option1;
		break;
	case 3: option = option1;
		break;
	case 4: option = option1;
		break;
	default: printf("\aInvalid option\n\n");
		exit(101);
	}
	return option;
}

void getdata(int* a, int* b)
{
	printf("Please enter two integer numbers: ");
	scanf("%d %d", a, b);
	return;
}

float calc(int option, int a, int b)
{
	float result;

	switch (option)
	{
	case 1: result = add(a, b);
		break;
	case 2: result = subtract(a, b);
		break;
	case 3: result = multiply(a, b);
		break;
	case 4: if (b == 0.0) {
		printf("\n\a\aError: ");

		printf("division by zero ***\n\n");
		exit(100);
	}
		  else
		result = quotient(a, b);
		break;
	default: printf("\aInvalid option\n");
		exit(101);
	}
	return result;
}

float add(int a, int b)
{
	int sum;
	sum = a + b;
	return sum;
}

float subtract(int a, int b)
{
	int S;
	S = a - b;
	return S;
}

float multiply(int a, int b)
{
	int M;
	M = a * b;
	return M;
}

float quotient(int a, int b)
{
	float Q;
	Q = (float)a / b;
	return Q;
}

void PrintResult(int a, int b, int option, float result, char* stdname, int stdnum)
{
	printf("\nPrinted at 함수\n성명=%s,\t학번=%8d", stdname, stdnum);
	switch (option)
	{
	case 1: printf("\n%d + %d = %6.2f\n", a, b, result);
		break;
	case 2: printf("\n%d - %d = %6.2f\n", a, b, result);
		break;
	case 3: printf("\n%d * %d = %6.2f\n", a, b, result);
		break;
	case 4: printf("\n%d / %d = %6.2f\n", a, b, result);
		break;
	default:
		break;
	}
	printf("END of Print.\n\n");
	return;
}*/