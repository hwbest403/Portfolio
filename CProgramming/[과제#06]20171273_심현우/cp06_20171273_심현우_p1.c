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
			r=calc(num); //r�� �Ҽ��� ���� calc�� ���� ���μ����� ����� ��� ������ ����Ʈ
			printend(num); //������ ����� ����Ʈ
		}
		if (num == 0) {
			printf("\n\nEnd of program\n");
			exit(100);
		}
	}

}

void getdata(int* a) //data�� �Է¹޴� �Լ�
{
	printf("Input an positive integer : ");
	scanf("%d", a);
}

void printend(int a) //�������� ���ڿ� ���� ������ ����Ʈ�ϴ� �Լ�
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

int quotient(int a, int b) //a�� �Ҽ��̰� b�� ����������� �������� ���� ������ b�� a�� ���� �� ���� �������� �Լ�
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

int prime1(int a, int b) //a�� �Ҽ��̰� b�� a�� ������ �������� a�� �������� �Լ�
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

int prime2(int a, int b) //a�� �Ҽ��̰� b�� a�� ������ �������� �������� ���� ������ b�� a�� ������ ��� ���������� Ƚ���� �������� �Լ�
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

int prime(int a) //a�� �Ҽ����� �Ǵ����ִ� �Լ�
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

int calc(int a) //�ٸ� �Լ����� �̿��Ͽ� ���������� ���μ����ظ� ����ϰ� print�ϸ� return�� �Ҽ� ������ ��ȯ�ϴ� �Լ�.
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
} //b���� ���� ������ 2���� ���ʷ� �Ҽ����� �Ǻ��ϰ� �Ҽ��̸� b�� �� ���� ���� ������������ �������� ���� ������ ������ ����� �ݺ������Ͽ� ���μ� ����.

int numberofmultiple(int a) //a�� �Ҽ��� ������ ���ϴ� �Լ�
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