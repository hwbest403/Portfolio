#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#pragma warning(disable: 4819)

//E[i,j]를 선택하기 위한 min함수
int min(int a, int b, int c);

void Edit_Distance(char* SS, char* TS,	int ins_cost, int del_cost, int sub_cost, int** Table, char** SR, char** OP, char** TR,	int* Mem_Allocated) {
	

	int i, j;
	int SN, TN;
	int a;
	//OP, SR, TR 배열의 사이즈
	int Maxsize = 0;
	SN = strlen(SS);
	SN = SN + 1;
	TN = strlen(TS);
	TN = TN + 1;
	//null char에서 null char의 cost는 0
	Table[0][0] = 0;
	//Table set.
	for (i = 1; i < SN; i++) {
		Table[i][0] = Table[i-1][0]+del_cost;
	}
	for (j = 1; j < TN; j++) {
		Table[0][j] = Table[0][j-1]+ins_cost;
	}
	for (i = 1; i < SN; i++) {
		for (j = 1; j < TN; j++) {
			//a는 substitution또는 기존 유지를 위한 cost.
			if (SS[i-1] != TS[j-1]) {
				a = sub_cost; //sub
			}
			else {
				a = 0; //기존유지.
			}
			//ins,del,sub중 작은 값으로 선택하여 Table 완성
			Table[i][j] = min(Table[i-1][j]+del_cost, Table[i][j-1]+ins_cost, Table[i-1][j-1]+a);
		}
	}
	i--, j--;
	//OP,SR,TR 사이즈를 구하기 위한 Back tracing.
	//Back-tracing하면서 방문하는 table의 개수가 배열의 크기가 됨.
	//back-tracing의 대한 자세한 내용은 뒤에 설명.
	while (i > 0) {
		if (i > 0 && j == 0) {
			i--;
			Maxsize++;
		}
		while (j > 0) {
			if (i == 0 && j > 0) {
				j--;
				Maxsize++;
				if (j == 0) {
					break;
				}
			}
			if (SS[i - 1] != TS[j - 1]) {
				a = sub_cost;
			}
			else {
				a = 0;
			}
			if (Table[i][j] == Table[i - 1][j] + del_cost && Table[i - 1][j] + del_cost < Table[i][j - 1] + ins_cost && Table[i - 1][j] + del_cost < Table[i - 1][j - 1] + a) {
				i--;
				Maxsize++;
			}
			else if (Table[i][j] == Table[i][j - 1] + ins_cost && Table[i][j - 1] + ins_cost < Table[i - 1][j] + del_cost && Table[i][j - 1] + ins_cost < Table[i - 1][j - 1] + a) {
				j--;
				Maxsize++;
			}
			else if (Table[i][j] == Table[i - 1][j - 1] + a && Table[i - 1][j - 1] + a < Table[i - 1][j] + del_cost && Table[i - 1][j - 1] + a < Table[i][j - 1] + ins_cost) {
				if (a == 0) {
					i--;
					j--;
					Maxsize++;
				}
				else {
					i--;
					j--;
					Maxsize++;
				}
			}
			else if (Table[i][j] == Table[i][j - 1] + ins_cost && Table[i][j - 1] + ins_cost == Table[i - 1][j] + del_cost) {
				if (ins_cost <= del_cost) {
					j--;
					Maxsize++;
				}
				else {
					i--;
					Maxsize++;
				}
			}
			else if (Table[i][j] == Table[i - 1][j - 1] + a && Table[i - 1][j - 1] + a == Table[i - 1][j] + del_cost) {
				i--;
				Maxsize++;
			}
			else if (Table[i][j] == Table[i - 1][j - 1] + a && Table[i - 1][j - 1] + a == Table[i][j - 1] + ins_cost) {
				j--;
				Maxsize++;
			}
			else if (Table[i - 1][j] + del_cost == Table[i][j - 1] + ins_cost && Table[i - 1][j - 1] + a == Table[i][j - 1] + ins_cost) {
				if (ins_cost <= del_cost) {
					j--;
					Maxsize++;
				}
				else {
					i--;
					Maxsize++;
				}
			}
		}
	}
	//배열 할당.
	*OP = new char [Maxsize+1];
	*SR = new char [Maxsize+1];
	*TR = new char [Maxsize+1];
	int memory = (Maxsize+1) * 3;
	*Mem_Allocated = memory;
	//총 메모리 계산.

	int count = 0;
	i = SN - 1, j = TN - 1;
	while (i > 0) {
		//j=0인 상황, Table에서 0열인데, 행은 0행이 아닌 경우, 0행이 될때까지, del을 수행해야함.
		if (i > 0 && j == 0) {
			OP[0][count] = 'd';
			SR[0][count] = SS[i - 1];
			TR[0][count] = '*';
			i--;
			count++;
		}
		while (j > 0) {
			//i=0인 상황, Table에서 0행인데, 열은 0열이 아닌 경우, 0열이 될때까지, ins수행.
			if (i == 0 && j > 0) {
				OP[0][count] = 'i';
				SR[0][count] = '*';
				TR[0][count] = TS[j - 1];
				j--;
				count++;
				if (j == 0) {
					break;
				}
			}
			//해당 table위치에서 sub구하기.
			if (SS[i - 1] != TS[j - 1]) {
				a = sub_cost;
			}
			else {
				a = 0;
			}
			//del수행이 ins, sub보다 작은 상황
			if (Table[i][j] == Table[i - 1][j] + del_cost && Table[i - 1][j] + del_cost < Table[i][j - 1] + ins_cost && Table[i - 1][j] + del_cost < Table[i - 1][j - 1] + a) {
				OP[0][count] = 'd';
				SR[0][count] = SS[i - 1];
				TR[0][count] = '*';
				i--;
				count++;
			}
			//ins수행이 del, sub보다 작은 상황.
			else if (Table[i][j] == Table[i][j-1] + ins_cost && Table[i][j-1] + ins_cost < Table[i-1][j] + del_cost && Table[i][j-1] + ins_cost < Table[i - 1][j - 1] + a) {
				OP[0][count] = 'i';
				SR[0][count] = '*';
				TR[0][count] = TS[j - 1];
				j--;
				count++;
			}
			//sub수행이 del, ins보다 작은 상황
			else if (Table[i][j] == Table[i-1][j - 1]+a && Table[i-1][j - 1] + a < Table[i - 1][j] + del_cost && Table[i-1][j - 1] + a < Table[i][j - 1] + ins_cost) {
				//이때는 a값을 통해 유지인지 sub인지 판단. a==0이면 유지.
				if (a == 0) {
					OP[0][count] = '.';
					SR[0][count] = SS[i - 1];
					TR[0][count] = TS[j - 1];
					i--;
					j--;
					count++;
				}
				//sub
				else {
					OP[0][count] = 's';
					SR[0][count] = SS[i - 1];
					TR[0][count] = TS[j - 1];
					i--;
					j--;
					count++;
				}
			}
			//ins랑 del는 같고 둘은 sub보다 작은 상황.
			else if (Table[i][j] == Table[i][j - 1] + ins_cost && Table[i][j - 1] + ins_cost == Table[i - 1][j] + del_cost) {
				//parent가 두개인 경우 cost를 통해 결정.
				if (ins_cost <= del_cost) {
					OP[0][count] = 'i';
					SR[0][count] = '*';
					TR[0][count] = TS[j - 1];
					j--;
					count++;
				}
				else {
					OP[0][count] = 'd';
					SR[0][count] = SS[i - 1];
					TR[0][count] = '*';
					i--;
					count++;
				}
			}
			//sub와 del가 같고 둘은 ins보다 작은상황. sub는 겹치지 않는 상황에만 선택이므로 del수행.
			else if (Table[i][j] == Table[i-1][j - 1] + a && Table[i-1][j - 1] + a == Table[i - 1][j] + del_cost) {
				OP[0][count] = 'd';
				SR[0][count] = SS[i - 1];
				TR[0][count] = '*';
				i--;
				count++;
			}
			//sub와 ins가 같고 둘은 del보다 작은상황.  sub는 겹치지 않는 상황에만 선택이므로 ins수행.
			else if (Table[i][j] == Table[i - 1][j - 1] + a && Table[i - 1][j - 1] + a == Table[i][j-1] + ins_cost) {
				OP[0][count] = 'i';
				SR[0][count] = '*';
				TR[0][count] = TS[j - 1];
				j--;
				count++;
			}
			//셋다 같은 상황
			else if (Table[i-1][j]+del_cost == Table[i][j - 1] + ins_cost && Table[i - 1][j - 1] + a == Table[i][j - 1] + ins_cost) {
				//cost 비교 후 수행
				if (ins_cost <= del_cost) {
					OP[0][count] = 'i';
					SR[0][count] = '*';
					TR[0][count] = TS[j - 1];
					j--;
					count++;
				}
				else {
					OP[0][count] = 'd';
					SR[0][count] = SS[i - 1];
					TR[0][count] = '*';
					i--;
					count++;
				}
			}
		}
	}
	//위는 backtracing의 결과이므로 결과를 위해 배열을 거꾸로 뒤집는다.
	char tmp;
	for (int k = 0; k < count / 2; k++) {
		tmp = OP[0][k];
		OP[0][k] = OP[0][count - 1 - k];
		OP[0][count - 1 - k] = tmp;
		tmp = SR[0][k];
		SR[0][k] = SR[0][count - 1 - k];
		SR[0][count - 1 - k] = tmp;
		tmp = TR[0][k];
		TR[0][k] = TR[0][count - 1 - k];
		TR[0][count - 1 - k] = tmp;
	}
	//할당 후 쓰지 않은 메모리는 null값으로 변경.
	for (int k = count; k < strlen(*OP); k++) {
		OP[0][k] = NULL;
	}
	for (int k = count; k < strlen(*SR); k++) {
		SR[0][k] = NULL;
	}
	for (int k = count; k < strlen(*TR); k++) {
		TR[0][k] = NULL;
	}
}

//a는 ins_cost, b는 del_cost, c는 substitution, ins_cost<=del_cost면 ins선택, ins_cost>del_cost면 del선택, sub는 둘다보다 작아야 선택.
int min(int a, int b, int c) {
	if (a <= b && a <= c) {
		return a;
	}
	else if (b < a && b <= c) {
		return b;
	}
	else if (c < a && c < b) {
		return c;
	}
}
