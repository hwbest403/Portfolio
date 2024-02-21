#include <stdio.h>
#include <stdlib.h>

int calccount(int a, int b, int num1, int num2, int num3, int num4, int num5, int num6, int num7, int num8, int num9, int num10);
int getnum(FILE* inFp, int* num1, int* num2, int* num3, int* num4, int* num5, int* num6, int* num7, int* num8, int* num9, int* num10);
int calc(int a, int b, int c);
int calcaverage(int a, int b, int num1, int num2, int num3, int num4, int num5, int num6, int num7, int num8, int num9, int num10);
int sum(int a, int b, int c);
void classify(FILE* clasFp1, FILE* clasFp2, FILE* clasFp3, FILE* clasFp4, int a);

void main()
{
	FILE* inFp, *clasFp, *clasFp1, *clasFp2, *clasFp3, *clasFp4;
	int rand1;
	int i,j;
	int k = 0;
	int num1, num2, num3, num4, num5, num6, num7, num8, num9, num10;
	int count1 = 0; int count2 = 0; int count3 = 0; int count4 = 0; int count5 = 0;
	float sum1 = 0; float sum2 = 0; float sum3 = 0; float sum4 = 0;
	float average1; float average2; float average3; float average4;

	inFp = fopen("c:\\test\\randnumber.txt", "w");
	if (inFp == NULL) {
		printf("file open error!\n");
		exit(100);
	}
	clasFp1 = fopen("c:\\test\\0~30.txt", "w");
	if (clasFp1 == NULL) {
		printf("file open error!");
		exit(100);
	}
	clasFp2 = fopen("c:\\test\\30~60.txt", "w");
	if (clasFp2 == NULL) {
		printf("file open error!");
		exit(100);
	}
	clasFp3 = fopen("c:\\test\\60~90.txt", "w");
	if (clasFp3 == NULL) {
		printf("file open error!");
		exit(100);
	}
	clasFp4 = fopen("c:\\test\\90~.txt", "w");
	if (clasFp4 == NULL) {
		printf("file open error!");
		exit(100);
	}

	while (k<1) {
		srand(20171273);
		for (j = 0; j < 10; j++) {
			for (i = 0; i < 10; i++) {
				rand1 = rand() % 101;
				fprintf(inFp, "%d ", rand1);
			}
			fprintf(inFp, "\n");
			i = 0;
		}
		k++;
	}
	fclose(inFp);

	clasFp= fopen("c:\\test\\randnumber.txt", "r");
	while (getnum(clasFp, &num1, &num2, &num3, &num4, &num5, &num6, &num7, &num8, &num9, &num10)) {

		classify(clasFp1, clasFp2, clasFp3, clasFp4, num1);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num2);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num3);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num4);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num5);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num6);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num7);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num8);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num9);
		classify(clasFp1, clasFp2, clasFp3, clasFp4, num10);

		count1 = count1 + calccount(0, 2, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		count2 = count2 + calccount(3, 5, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		count3 = count3 + calccount(6, 8, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		count4 = count4 + calccount(9, 10, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		sum1 = sum1 + calcaverage(0, 2, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		sum2 = sum2 + calcaverage(3, 5, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		sum3 = sum3 + calcaverage(6, 8, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
		sum4 = sum4 + calcaverage(9, 10, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
	}
	average1 = sum1 / count1;
	average2 = sum2 / count2;
	average3 = sum3 / count3;
	average4 = sum4 / count4;

	printf("처리결과\n");
	printf(" 0 ~  30 미만: count = %d, 평균 = %4.1f\n", count1, average1);
	printf("30 ~  60 미만: count = %d, 평균 = %4.1f\n", count2, average2);
	printf("60 ~  90 미만: count = %d, 평균 = %4.1f\n", count3, average3);
	printf("90 ~ 100 미만: count = %d, 평균 = %4.1f\n", count4, average4);
	printf("범위외 숫자의 count = %d\n", count5);

	fclose(clasFp);
}

int getnum(FILE* inFp, int* num1, int* num2, int* num3, int* num4, int* num5, int* num6, int* num7, int* num8, int* num9, int* num10) {
	int ioResult;
	ioResult = fscanf(inFp, " %d %d %d %d %d %d %d %d %d %d ", num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);
	if (ioResult == EOF) {
		return 0;
	}
	else return 1;
}

int calccount(int a, int b, int num1, int num2, int num3, int num4, int num5, int num6, int num7, int num8, int num9, int num10) {
	int result;
	result = calc(num1, a, b) + calc(num2, a, b) + calc(num3, a, b) + calc(num4, a, b) + calc(num5, a, b) + calc(num6, a, b) + calc(num7, a, b) + calc(num8, a, b) + calc(num9, a, b) + calc(num10, a, b);
	return result;
}

int calc(int a, int b, int c) {
	int i;
	int count=0;
	for (i = b; i <= c; i++) {
		if (a / 10 == i) {
			count = count + 1;
		}
		else {
			count = count;
		}
	}
	return count;
}

int calcaverage(int a, int b, int num1, int num2, int num3, int num4, int num5, int num6, int num7, int num8, int num9, int num10) {
	int sum1 = 0;
	sum1 = sum(num1, a, b) + sum(num2, a, b) + sum(num3, a, b) + sum(num4, a, b) + sum(num5, a, b) + sum(num6, a, b) + sum(num7, a, b) + sum(num8, a, b) + sum(num9, a, b) + sum(num10, a, b);
	return sum1;
}

int sum(int a, int b, int c) {
	int i;
	int sum = 0;
	for (i = b; i <= c; i++) {
		if (a / 10 == i) {
			sum = sum + a;
		}
		else {
			sum = sum;
		}
	}
	return sum;
}

void classify(FILE* clasFp1, FILE *clasFp2, FILE* clasFp3, FILE* clasFp4, int a) {
	if (0 <= a&&a<30) {
		fprintf(clasFp1, "%d ", a);
	}
	else if (30 <= a&&a < 60) {
		fprintf(clasFp2, "%d ", a);
	}
	else if (60 <= a&&a < 90) {
		fprintf(clasFp3, "%d ", a);
	}
	else if (60 <= a) {
		fprintf(clasFp4, "%d ", a);
	}
	return;
}