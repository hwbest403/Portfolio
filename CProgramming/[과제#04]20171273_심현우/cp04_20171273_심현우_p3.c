#include <stdio.h>

void getdataC(float* a);
void CtoF(float a);
void getdataF(float* a);
void FtoC(float a);

void main()
{
	float a;
	float b;

	int i = 0;
	while (i < 2) {

		getdataC(&a);
		CtoF(a);

		getdataF(&b);
		FtoC(b);

		i++;
	}
	return;
}

void getdataC (float* a)
{
	printf("섭씨 온도를 입력하시기 바랍니다 : ");
	scanf("%f", a);
	return;
}

void CtoF(float a)
{
	float F;
	F = ((float)9 / 5) * a + 32;
	printf("섭씨 온도는 %4.2f 입니다.\n\n", F);
	return;
}

void getdataF(float* b)
{
	printf("화씨 온도를 입력하시기 바랍니다 : ");
	scanf("%f", b);
	return;
}

void FtoC(float b)
{
	float C;
	C = ((float)5 / 9) * (b - 32);
	printf("섭씨 온도는 %4.2f 입니다.\n\n", C);
	return;
}