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
		printf("���� �� ����ϴ� ���� : ");
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

	printf("\n �Է��� ���� �迭 data :\n");
	print_array(parr, arrSize, LineSize);

	sort_reorder(parr, arrSize);

	printf("\n ũ�� ������ ���� sort�� ���� �迭 data :\n");
	print_array(parr, arrSize, LineSize);

	printf("\n");

	return;
}

int* input_integer(int* arrSize) {

	int i;
	int* parr;

	while (1) {
		printf("�Է��� �����迭�� ũ��� = ? ");
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