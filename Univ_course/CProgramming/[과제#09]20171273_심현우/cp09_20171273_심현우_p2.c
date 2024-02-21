#include <stdio.h>
#include <stdlib.h>

void calGcdLcm(int num1, int num2, int* gcd, int* lcm);

void main() {

	int num1;
	int num2;
	int gcd, lcm;
	
	printf("Enter the 1st number : ");
	scanf("%d", &num1);
	printf("Enter the 2nd number : ");
	scanf("%d", &num2);
	calGcdLcm(num1, num2, &gcd, &lcm);

	printf("GCD of %d and %d is %d\n", num1, num2, gcd);
	printf("LCM of %d and %d is %d\n", num1, num2, lcm);

	return;
}

void calGcdLcm(int num1, int num2, int* gcd, int* lcm) {

	int a, b;
	if (num1 > num2) {
		a = num1;
		b = num2;
		while (1) {
			*gcd = num1 % num2;
			if (*gcd == 0) {
				*gcd = num2;
				break;
			}
			num1 = num2;
			num2 = *gcd;
		}
	}
	else if (num2 > num1) {
		a = num1;
		b = num2;
		while (1) {
			*gcd = num2 % num1;
			if (*gcd == 0) {
				*gcd = num1;
				break;
			}
			num2 = num1;
			num1 = *gcd;
		}
	}
	else {
		a = num1;
		b = num2;
		*gcd = num1;
	}
	*lcm = (a * b) / *gcd;
	return;
}