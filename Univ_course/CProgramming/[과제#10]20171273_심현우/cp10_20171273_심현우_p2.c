#include <stdio.h>
#include <stdlib.h>
#define EOF -1

void inverseOrder(int *arr, int arrSize);
void printarray(int arr[][8], int rownumber);


void main() {

	int a;
	int b=1;
	int* parr[4];
	int data[4][8] = { {838,758,113,515,51,627,10,419},{212,86,749,767,84,60,225,543},{89,183,137,566,966,978,495,311},{367,54,31,145,882,736,524,505} };
	int i;

	printf("Before Reorder\n");
	printarray(data, 0);
	printarray(data, 1);
	printarray(data, 2);
	printarray(data, 3);

	parr[0] = (int*)malloc(8 * sizeof(int));
	parr[1] = (int*)malloc(8 * sizeof(int));
	parr[2] = (int*)malloc(8 * sizeof(int));
	parr[3] = (int*)malloc(8 * sizeof(int));
	
	while (1) {
		printf("\nEnter the row index (0~3) : ");
		b=scanf("%d", &a);
		if (b == -1) {  //CTRL+Z를 세번 입력해야 프로그램이 종료되는 것으로 확인했습니다.
			break;      //구글링으로 찾아봤지만 어떻게 고쳐야하는지 잘 모르겠습니다.
		}
		else {
			if (a < 0) {
				continue;
			}
			else if (a > 3) {
				continue;
			}
			else if (0 <= a <= 3) {
				for (i = 0; i < 8; i++) {
					parr[a][i] = data[a][i];
				}
				printf("\n%d_th row after inver ordering\n", a);
				inverseOrder(parr[a], 8);
				for (i = 0; i < 8; i++) {
					data[a][i] = parr[a][i];
				}
				printarray(data, a);
				continue;
			}
		}
	}
	
	printf("\nAfter reordering\n");
	printarray(data, 0);
	printarray(data, 1);
	printarray(data, 2);
	printarray(data, 3);
}

void inverseOrder(int *arr, int arrSize) {

	int i;
	int temp;

	for (i = 0; i < arrSize / 2; i++) {
		temp = *(arr + i);
		*(arr + i) = *(arr + arrSize - 1 - i);
		*(arr + arrSize - 1 - i) = temp;
	}
}

void printarray(int arr[][8], int rownumber) {
	
	int i;

	for (i = 0; i < 8; i++) {
		printf("%6d", *(*(arr+rownumber)+i));
	}
	printf("\n");
	
	return;
}