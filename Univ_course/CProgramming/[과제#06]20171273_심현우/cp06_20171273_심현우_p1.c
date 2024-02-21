#include <stdio.h>
#include <stdlib.h>

void getdata(int* a);
void printend(int a);
int prime(int a);
int quotient(int a, int b);
int prime1(int a, int b);
int prime2(int a, int b);
int calc(int a);
int numberofmultiple(int a);

void main()
{
	
	int num;
	int p;
	int r;

	for (p = 0;; p++) {
		getdata(&num);
		if (num != 0) {
			r=calc(num); //r은 소수의 개수 calc를 통해 소인수분해 계산후 계산 과정만 프린트
			printend(num); //마지막 결과를 프린트
		}
		if (num == 0) {
			printf("\n\nEnd of program\n");
			exit(100);
		}
	}

}

void getdata(int* a) //data를 입력받는 함수
{
	printf("Input an positive integer : ");
	scanf("%d", a);
}

void printend(int a) //마지막에 숫자에 대한 성질을 프린트하는 함수
{
	int prime;
	int b = 0;
	int i = 0;
	if (a <= 1) {
		printf("\nIt is a invalid number !\n\n");
	}
	else {
		for (i = 1; i <= a; i++)
		{
			if (a % i == 0)
			{
				b++;
			}
		}
		if (b == 2)
		{
			printf("It is a prime number !\n\n");
		}
		else
		{
			printf("It is a composite number !\n\n");
		}
	}
	return;
}

int quotient(int a, int b) //a가 소수이고 b로 나누어떨이지면 나머지가 없을 때까지 b를 a로 나눈 후 몫을 가져오는 함수
{
	int result1 = 1;
	int j = 0;
	if (b == 1) {
		result1 = 1;
	}
	else {
		if (prime(a) != 0) {
			for (j = 0; ; j++) {
				if (b % a == 0) {
					b = b / a;
				}
				else {
					break;
				}
			}
		}
		else {
			result1 = 1;
		}
	}
	if (j == 0) {
		result1 = 1;
	}
	else {
		result1 = b;
	}
	return result1;
}

int prime1(int a, int b) //a가 소수이고 b가 a로 나누어 떨이지면 a를 가져오는 함수
{
	int result2 = 0;
	int j = 0;
	if (b == 1) {
		result2 = 0;
	}
	else {
		if (prime(a) != 0) {
			if (b % a == 0) {
				result2 = a;
			}
			else {
				result2 = 0;
			}
		}
		else {
			result2 = 0;
		}
	}
	return result2;
}

int prime2(int a, int b) //a가 소수이고 b가 a로 나누어 떨어지면 나머지가 없을 때까지 b를 a로 나누고 몇번 나누었는지 횟수를 가져오는 함수
{
	int result3 = 0;
	int j = 0;
	if (b == 1) {
		result3 = 0;
	}
	else {
		if (prime(a) != 0) {
			for (j = 0; ; j++) {
				if (b % a == 0) {
					b = b / a;
				}
				else {
					break;
				}
			}
		}
		else {
			result3 = 0;
		}
	}
	if (j == 0) {
		result3 = 0;
	}
	else {
		result3 = j;
	}
	return result3;
}

int prime(int a) //a가 소수인지 판단해주는 함수
{
	int prime;
	int b = 0;
	int i = 0;

	for (i = 1; i <= a; i++)
	{
		if (a % i == 0)
		{
			b++;
		}
	}
	if (a <= 0) {
		prime = 0;
	}
	if (b == 2)
	{
		prime = a;
	}
	else
	{
		prime = 0;
	}
	return prime;
}

int calc(int a) //다른 함수들을 이용하여 마지막으로 소인수분해를 계산하고 print하며 return은 소수 개수로 반환하는 함수.
{
	int i;
	int k;
	int m;
	int n;
	int a1;
	int r;

	a1 = a;
	printf("%d = ", a);
	for (i = 2; i <= a; i++) {
		k = prime1(i, a);
		if (k != 0) {
			printf("%d", k);
		}
		m = prime2(i, a);
		n = quotient(i, a1);
		if (n != 1) {
			a1 = n;
			if (m != 0) {
				if (m == 1) {
					printf("*");
				}
				else {
					printf("^%d*", m);
				}
			}
		}
		if (n == 1) {
			if (m == 1) {
				printf("\n");
			}
			if (m >= 2) {
				printf("^%d\n", m);
			}
		}
	}
	r = numberofmultiple(a);
	return r;
} //b보다 작은 수들을 2부터 차례로 소수인지 판별하고 소수이면 b를 그 수로 나눠 나눠떨어지면 나머지가 없을 때까지 나누는 계산을 반복실행하여 소인수 분해.

int numberofmultiple(int a) //a의 소수의 개수를 구하는 함수
{
	int i;
	int m;
	int m1=0;
	int j;

	for (i = 2; i <= a; i++) {
		m = prime2(i, a);
		for (j = 1; j <= m;j++) {
			m1++;
		}
	}
	return m1;
}