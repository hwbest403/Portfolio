#include <stdio.h>
#include <stdlib.h>

void main() {

	int a, b, r;
	int* pa = &a;
	int* pb = &b;
	int* pr = &r;

	printf("Enter the first number : ");
	scanf("%d", pa);
	printf("Enter the second number : ");
	scanf("%d", pb);
	*pr = *pa + *pb;
	printf("\n%d + %d is %d", *pa, *pb, *pr);
	*pr = *pa - *pb;
	printf("\n%d - %d is %d", *pa, *pb, *pr);
	*pr = *pa * *pb;
	printf("\n%d * %d is %d", *pa, *pb, *pr);
	*pr = *pa / *pb;
	printf("\n%d / %d is %d", *pa, *pb, *pr);
	*pr = *pa % *pb;
	printf("\n%d %% %d is %d\n", *pa, *pb, *pr);
	return;
}