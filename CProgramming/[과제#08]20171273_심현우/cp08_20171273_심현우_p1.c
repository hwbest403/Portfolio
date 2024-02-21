#include <stdio.h>
#include <stdlib.h>
#define ROWS 2
#define COLUMNS 10

void selectionsort2(int table[][COLUMNS], int last);

void main() {
	int table[ROWS][COLUMNS] = { {18,237,35,5,76,103,189,22,156,49}, {90,47,105,25,739,26,38,110,31,245} };
	
	printf("Original Table\n");
	int column1;
	for (column1 = 0; column1 < COLUMNS; column1++) {
		printf("id number;%3d, mark; %3d :\n", table[0][column1], table[1][column1]);
	}

	printf("\nAscending sorted table for the first column is as follows.\n");
	
	selectionsort2(table, COLUMNS-1);
	int column2;
	for (column2 = 0; column2 < COLUMNS; column2++) {
		printf("id number;%3d, mark; %3d :\n", table[0][column2], table[1][column2]);
	}

	return;
}

void selectionsort2(int table[][COLUMNS], int last) {

	int smallest, tempData, current, walk;
	int row;

	for (current = 0; current < last; current++) {
		smallest = current;
		for (walk = current + 1; walk <= last; walk++)
			if (table[0][walk] < table[0][smallest])
				smallest = walk;

		for (row = 0; row < ROWS; row++) {
			tempData = table[row][current];
			table[row][current] = table[row][smallest];
			table[row][smallest] = tempData;
		}
		}
	return;
}