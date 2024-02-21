#include <stdio.h>
#include <math.h>
#define BOUND 0.001 //BOUND를 0.001로 해준 이유는 과제의 예시를 보면 루트2를 1.4142로 계산하고 있다.
//루트2는 1.4142로 끝나지 않는 무한 소수인데 입력을 할 수 없기에 소수 5자리 이하는 무시해 주는 것으로 볼수있다.

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
	printf("직선의 함수식을 입력하기 바랍니다.\n");
	printf("y = ax + b\n");
	printf("기울기 a = ");
	scanf("%lf", a);
	printf("교차점 b = ");
	scanf("%lf", b);
}

void getdataofcircle(double* a, double* b, double* c)
{
	printf("\n원의 함수식을 입력하기 바랍니다.\n");
	printf("(x - cx)^2 + (y - cy)^2 = r^2\n");
	printf("cx = ");
	scanf("%lf", a);
	printf("cy = ");
	scanf("%lf", b);
	printf("반지름 r = ");
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

	D = j * j - 4 * i * k; //D계산식에서 루트2의 소수점 5자리 이하를 무시해줬다. 여기서 반지름 r은 e로 쓰였고
	//e는 D의 값에서 +(a^2+1)*e^2만큼 관여한다. 소수점 아래 5자리부터 무시했으므로 D의 BOUND를 0.001 즉 3자리 밑으로 계산되어진 것들을
	//0으로 같게 취급해주어 계산에서 발생하는 오차에 한계치로 정해주었다.

	if (fabs(D) <= BOUND) {
		root1 = -j / (2.0 * i);
		if (root1 = 0) //여기 계산에서 root1이 0이 될 경우 식으로 인해 -0으로 값이 출력되는데 이를 방지하기 위해 +0으로 다시 지정해줌.
		{
			root1 = 0;
		}
		else {
			root1 = root1;
		}
		rooty1 = a * root1 + b;
		printf("직선 라인은 원에 접합니다.\n");
		printf("(%6.3lf, %6.3lf)\n", root1, rooty1);
	}
	else if (D > 0) {
		D = sqrt(D);
		root1 = (-j - D) / (2.0 * i);
		root2 = (-j + D) / (2.0 * i);
		rooty1 = a * root1 + b;
		rooty2 = a * root2 + b;
		printf("두 함수에는 두개의 교차점이 있습니다.\n");
		printf("(%6.3lf, %6.3lf), (%6.3lf, %6.3lf)\n", root1, rooty1, root2, rooty2);
	}
	else {
		printf("두 함수의 교차점이 없습니다.\n");
	}
}