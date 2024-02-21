#include <stdio.h>
#include <stdlib.h>

int** transpose(int** matrix, int m, int n);
void printMatrix(int** matrix, int m, int n);

void main() {

	int rand1;
	int row, col;
	int** matrix;
	int** parr;
	int r, c;

	printf("Number of Rows : ");
	scanf("%d", &row);
	printf("Number of Cols : ");
	scanf("%d", &col);
	printf("seed锅龋 %d肺 积己等 Matrix\n", 20171273);

	srand(20171273);

	matrix = (int**)malloc(row * sizeof(int*));
	matrix[0] = malloc(row * col * sizeof(int));

	for (r = 1; r < row; r++) {
		matrix[r] = matrix[r - 1] + col;
	}

	for (r = 0; r < row; r++) {
		for (c = 0; c < col; c++) {
			rand1 = rand() % 100 + 1;
			matrix[r][c] = rand1;
		}
	}

	printMatrix(matrix, col, row);
	parr = transpose(matrix, col, row);
	printf("\nTranspose等 Matrix\n");
	printMatrix(parr, row, col);

	return;
}

int** transpose(int** matrix, int m, int n) {

	int r, c;
	int** parr;
	
	parr = (int**)malloc(m * sizeof(int*));
	parr[0] = malloc(n * m * sizeof(int));

	for (r = 1; r < m; r++) {
		parr[r] = parr[r - 1] + m;
	}

	for (r = 0; r < n; r++) {
		for (c = 0; c < m; c++) {
			parr[c][r] = matrix[r][c];
		}
	}

	return parr;
}

void printMatrix(int** matrix, int m, int n) {

	int r, c;
	for (r = 0; r < n; r++) {
		for (c = 0; c < m; c++) {
			printf("%3d", matrix[r][c]);
		}
		printf("\n");
	}

	return;
}