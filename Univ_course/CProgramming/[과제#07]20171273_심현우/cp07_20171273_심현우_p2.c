#include <stdio.h>
#include <stdlib.h>



void main() {

	FILE* inFp, * outFp;
	int num1, amount, reorder, min;
	float price;
	int ioResult;
	int order;

	inFp = fopen("c:\\test\\�����\\input.txt", "r");
	if (inFp == NULL) {
		printf("file open error!\n");
		exit(100);
	}

	outFp = fopen("c:\\test\\�����\\output.txt", "w");
	if (outFp == NULL) {
		printf("file open error!\n");
		exit(100);
	}

	printf("\tInventory Report\n");
	fprintf(outFp, "\tInventory Report\n");
	printf("��ǰ��ȣ	 ����  ���  ���ֹ�����	�ּ��ֹ���	�ֹ���\n");
	fprintf(outFp, "��ǰ��ȣ	 ����  ���  ���ֹ�����	�ּ��ֹ���	�ֹ���\n");

	while (1) {
		ioResult = fscanf(inFp,"%d %f %d %d %d", &num1, &price, &amount, &reorder, &min);
		if (ioResult == EOF) {
			return 0;
		}

		if (amount > reorder) {
			order = 0;
		}
		else {
			order = reorder - (amount - min);
		}

		printf("  %04d		%5.2f    %2d       %d		    %d		  %2d\n", num1, price, amount, reorder, min, order);
		fprintf(outFp, "  %04d	%5.2f     %2d	%d	      %d		  %2d\n", num1, price, amount, reorder, min, order);
	}
	
	printf("End of Report");
}

