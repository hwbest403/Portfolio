#include <stdio.h>

void getdata (int* a, int* b);
void add (int a, int b);
void subtract (int a, int b);
void multiply (int a, int b);
void quotient (int a, int b);
void remainder (int a, int b);

void main()
{
	int a, b;
	getdata(&a, &b);
	add(a, b);
	subtract(a, b);
	multiply(a, b);
	quotient(a, b);
	remainder(a, b);

	return;

}

void getdata(int* a, int* b)
{
	printf("Please enter two integer numbers: ");
	scanf("%d %d", a, b);
	return;
}

void add (int a, int b)
{
	int sum;
	sum = a + b;
	printf("µ¡¼À °á°ú´Â : %d %d=%4d\n", a, b, sum);
	return;
}

void subtract (int a, int b)
{
	int S;
	S = a - b;
	printf("»¬¼À °á°ú´Â : %d %d=%4d\n", a, b, S);
	return;
}

void multiply (int a, int b)
{
	int M;
	M = a * b;
	printf("°ö¼À °á°ú´Â : %d %d=%4d\n", a, b, M);
	return;
}

void quotient (int a, int b)
{
	int Q;
	Q = a / b;
	printf("³ª´« ¸òÀÇ °ª: %d %d=%4d\n", a, b, Q);
	return;
}

void remainder (int a, int b)
{
	int R;
	R = a % b;
	printf("³ª¸ÓÁö °ªÀº : %d %d=%4d\n", a, b, R);
	return;
}