#include <stdio.h>
#include <stdlib.h>

int* input_integer(int* arrSize);
void sort_reorder(int* arr, int arrSize);
void print_array(int* arr, int arrSize, int lineNo);

void main() {

	int LineSize;
	int* parr = NULL;
	int arrSize;

	while (1) {
		printf("라인 당 출력하는 개수 : ");
		scanf("%d", &LineSize);
		printf("\n");
		if (LineSize <= 0) {
			continue;
		}
		else {
			break;
		}
	}

	parr = input_integer(&arrSize);

	printf("\n 입력한 정수 배열 data :\n");
	print_array(parr, arrSize, LineSize);

	sort_reorder(parr, arrSize);

	printf("\n 크기 순서에 따라 sort된 정수 배열 data :\n");
	print_array(parr, arrSize, LineSize);

	printf("\n");

	return;
}

int* input_integer(int* arrSize) {

	int i;
	int* parr;

	while (1) {
		printf("입력할 정수배열의 크기는 = ? ");
		scanf("%d", arrSize);
		if (*arrSize <= 0) {
			printf("\n");
			continue;
		}
		else {
			break;
		}
	}

	parr = (int*)malloc(*arrSize * sizeof(int));
	
	for (i = 0; i < *arrSize; i++) {
		scanf("%d", &parr[i]);
	}
	return parr;
}

void sort_reorder(int* arr, int arrSize) {

	int biggest, tempData, current, walk;

	for (current = 0; current < arrSize; current++) {
		biggest = current;
		for (walk = current + 1; walk < arrSize; walk++) {
			if (arr[walk] > arr[biggest]) {
				biggest = walk;
			}
		}
		tempData = arr[current];
		arr[current] = arr[biggest];
		arr[biggest] = tempData;
	}
	return;
}

void print_array(int* arr, int arrSize, int lineNo) {
	
	int i;

	for (i = 0; i < arrSize; i++) {
		if ((i % lineNo) == 0)
			printf("\n");
		printf("%4d ", arr[i]);
	}
	printf("\n");
	return;
}