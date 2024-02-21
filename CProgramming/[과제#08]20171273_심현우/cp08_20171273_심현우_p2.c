/*#include <stdio.h>
#include <stdlib.h>

int getstring(char string[]);
void printstring(char string[], int sizestring);
void reversestring(char string[], int sizestring);

void main() {

	int size;
	char string[250];
	
	while (1) {
		printf("문자열을 입력하시기 바랍니다.\n");
		printf("(단, 종료는 CRTL-Z) : ");

		size = getstring(string);
		if (size == -1) {
			exit(101);
		}
		reversestring(string, size);
		printstring(string, size);
	}

	return;
}

int getstring(char string[]) {
	
	int size=0;
	int i = 0;
	char ch;
	
	while (1) {
		ch = getchar();
		if (ch == EOF) {
			size = -1;
			break;
		}
		else if (ch == '\n') {
			break;
		}
		else {
			size++;
		}
		string[i] = ch;
		i++;
	}
	string[i] = '\0';
	return size;
}

void printstring(char string[], int sizestring) {

	int i;
	
	printf("역으로 배열한 문자열은 : ");

	for (i = 0; i <= sizestring+1; i++) {
		putchar(string[i]);
	}
	printf("\n");
}

void reversestring(char string[], int sizestring) {
	int i;
	char temp;

	for (i = 0; i < sizestring/2; i++) {
		temp = string[i];
		string[i] = string[sizestring - 1 - i];
		string[sizestring - 1 - i] = temp;
	}

	string[sizestring] = '\0';
	string[sizestring+1] = '\n';
	
}
*/