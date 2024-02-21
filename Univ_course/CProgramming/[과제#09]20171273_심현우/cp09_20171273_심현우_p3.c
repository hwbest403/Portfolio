#include <stdio.h>
#include <stdlib.h>

int getTime(long time[], int max_size);
int secToHours(long time, int* hours, int* minutes, int* seconds);

void main() {

	long time[10];
	int size;
	int i;
	int hours, minutes, seconds;
	size = getTime(time, 10);
	for (i = 0; i < size; i++) {
		secToHours(time[i], &hours, &minutes, &seconds);
		if (time[i] == 0) {
			break;
		}
		printf("%ld = %2d:%02d:%02d\n", time[i], hours, minutes, seconds);
	}
	printf("\n E N D  O F  P R O G R A M\n");
}

int getTime(long time[], int max_size) {
	
	long a;
	int i;
	for (i = 0; i < max_size; i++) {
		printf("변환할 시간을 입력하기 바랍니다.");
		scanf("%d", &a);
		time[i] = a;
		if (a == 0) {
			break;
		}
	}
	i = i + 1;
	if (i == max_size + 1) {
		i = max_size;
	}
	return i;
}

int secToHours(long time, int* hours, int* minutes, int* seconds) {
	long localTime;
	localTime = time;
	*seconds = localTime % 60;
	localTime = localTime / 60;
	*minutes = localTime % 60;
	*hours = localTime / 60;
	if (*hours >= 24) return 0;
	else return 1;
}