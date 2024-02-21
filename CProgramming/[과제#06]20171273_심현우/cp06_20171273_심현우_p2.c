#include <stdio.h>
#include <math.h>
#define BOUND 0.001 //BOUND�� 0.001�� ���� ������ ������ ���ø� ���� ��Ʈ2�� 1.4142�� ����ϰ� �ִ�.
//��Ʈ2�� 1.4142�� ������ �ʴ� ���� �Ҽ��ε� �Է��� �� �� ���⿡ �Ҽ� 5�ڸ� ���ϴ� ������ �ִ� ������ �����ִ�.

void getdataofline(double* a, double* b);
void getdataofcircle(double* a, double* b, double* c);
void calc(double a, double b, double c, double d, double e);

void main()
{
	double a1, a2, b1, b2, b3;
	getdataofline(&a1, &a2);
	getdataofcircle(&b1, &b2, &b3);
	calc(a1, a2, b1, b2, b3);
	return;
}

void getdataofline(double* a, double* b)
{
	printf("������ �Լ����� �Է��ϱ� �ٶ��ϴ�.\n");
	printf("y = ax + b\n");
	printf("���� a = ");
	scanf("%lf", a);
	printf("������ b = ");
	scanf("%lf", b);
}

void getdataofcircle(double* a, double* b, double* c)
{
	printf("\n���� �Լ����� �Է��ϱ� �ٶ��ϴ�.\n");
	printf("(x - cx)^2 + (y - cy)^2 = r^2\n");
	printf("cx = ");
	scanf("%lf", a);
	printf("cy = ");
	scanf("%lf", b);
	printf("������ r = ");
	scanf("%lf", c);
}

void calc(double a, double b, double c, double d, double e)
{
	double i, j, k;
	double D;
	double root1, root2;
	double rooty1, rooty2;
	i = a * a + 1;
	j = 2 * a * b - 2 * a * d - 2 * c;
	k = b * b + c * c + d * d - 2 * b * d - e * e;

	D = j * j - 4 * i * k; //D���Ŀ��� ��Ʈ2�� �Ҽ��� 5�ڸ� ���ϸ� ���������. ���⼭ ������ r�� e�� ������
	//e�� D�� ������ +(a^2+1)*e^2��ŭ �����Ѵ�. �Ҽ��� �Ʒ� 5�ڸ����� ���������Ƿ� D�� BOUND�� 0.001 �� 3�ڸ� ������ ���Ǿ��� �͵���
	//0���� ���� ������־� ��꿡�� �߻��ϴ� ������ �Ѱ�ġ�� �����־���.

	if (fabs(D) <= BOUND) {
		root1 = -j / (2.0 * i);
		if (root1 = 0) //���� ��꿡�� root1�� 0�� �� ��� ������ ���� -0���� ���� ��µǴµ� �̸� �����ϱ� ���� +0���� �ٽ� ��������.
		{
			root1 = 0;
		}
		else {
			root1 = root1;
		}
		rooty1 = a * root1 + b;
		printf("���� ������ ���� ���մϴ�.\n");
		printf("(%6.3lf, %6.3lf)\n", root1, rooty1);
	}
	else if (D > 0) {
		D = sqrt(D);
		root1 = (-j - D) / (2.0 * i);
		root2 = (-j + D) / (2.0 * i);
		rooty1 = a * root1 + b;
		rooty2 = a * root2 + b;
		printf("�� �Լ����� �ΰ��� �������� �ֽ��ϴ�.\n");
		printf("(%6.3lf, %6.3lf), (%6.3lf, %6.3lf)\n", root1, rooty1, root2, rooty2);
	}
	else {
		printf("�� �Լ��� �������� �����ϴ�.\n");
	}
}