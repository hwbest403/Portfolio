#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#pragma warning(disable: 4819)

//E[i,j]�� �����ϱ� ���� min�Լ�
int min(int a, int b, int c);

void Edit_Distance(char* SS, char* TS,	int ins_cost, int del_cost, int sub_cost, int** Table, char** SR, char** OP, char** TR,	int* Mem_Allocated) {
	

	int i, j;
	int SN, TN;
	int a;
	//OP, SR, TR �迭�� ������
	int Maxsize = 0;
	SN = strlen(SS);
	SN = SN + 1;
	TN = strlen(TS);
	TN = TN + 1;
	//null char���� null char�� cost�� 0
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
			//a�� substitution�Ǵ� ���� ������ ���� cost.
			if (SS[i-1] != TS[j-1]) {
				a = sub_cost; //sub
			}
			else {
				a = 0; //��������.
			}
			//ins,del,sub�� ���� ������ �����Ͽ� Table �ϼ�
			Table[i][j] = min(Table[i-1][j]+del_cost, Table[i][j-1]+ins_cost, Table[i-1][j-1]+a);
		}
	}
	i--, j--;
	//OP,SR,TR ����� ���ϱ� ���� Back tracing.
	//Back-tracing�ϸ鼭 �湮�ϴ� table�� ������ �迭�� ũ�Ⱑ ��.
	//back-tracing�� ���� �ڼ��� ������ �ڿ� ����.
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
	//�迭 �Ҵ�.
	*OP = new char [Maxsize+1];
	*SR = new char [Maxsize+1];
	*TR = new char [Maxsize+1];
	int memory = (Maxsize+1) * 3;
	*Mem_Allocated = memory;
	//�� �޸� ���.

	int count = 0;
	i = SN - 1, j = TN - 1;
	while (i > 0) {
		//j=0�� ��Ȳ, Table���� 0���ε�, ���� 0���� �ƴ� ���, 0���� �ɶ�����, del�� �����ؾ���.
		if (i > 0 && j == 0) {
			OP[0][count] = 'd';
			SR[0][count] = SS[i - 1];
			TR[0][count] = '*';
			i--;
			count++;
		}
		while (j > 0) {
			//i=0�� ��Ȳ, Table���� 0���ε�, ���� 0���� �ƴ� ���, 0���� �ɶ�����, ins����.
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
			//�ش� table��ġ���� sub���ϱ�.
			if (SS[i - 1] != TS[j - 1]) {
				a = sub_cost;
			}
			else {
				a = 0;
			}
			//del������ ins, sub���� ���� ��Ȳ
			if (Table[i][j] == Table[i - 1][j] + del_cost && Table[i - 1][j] + del_cost < Table[i][j - 1] + ins_cost && Table[i - 1][j] + del_cost < Table[i - 1][j - 1] + a) {
				OP[0][count] = 'd';
				SR[0][count] = SS[i - 1];
				TR[0][count] = '*';
				i--;
				count++;
			}
			//ins������ del, sub���� ���� ��Ȳ.
			else if (Table[i][j] == Table[i][j-1] + ins_cost && Table[i][j-1] + ins_cost < Table[i-1][j] + del_cost && Table[i][j-1] + ins_cost < Table[i - 1][j - 1] + a) {
				OP[0][count] = 'i';
				SR[0][count] = '*';
				TR[0][count] = TS[j - 1];
				j--;
				count++;
			}
			//sub������ del, ins���� ���� ��Ȳ
			else if (Table[i][j] == Table[i-1][j - 1]+a && Table[i-1][j - 1] + a < Table[i - 1][j] + del_cost && Table[i-1][j - 1] + a < Table[i][j - 1] + ins_cost) {
				//�̶��� a���� ���� �������� sub���� �Ǵ�. a==0�̸� ����.
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
			//ins�� del�� ���� ���� sub���� ���� ��Ȳ.
			else if (Table[i][j] == Table[i][j - 1] + ins_cost && Table[i][j - 1] + ins_cost == Table[i - 1][j] + del_cost) {
				//parent�� �ΰ��� ��� cost�� ���� ����.
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
			//sub�� del�� ���� ���� ins���� ������Ȳ. sub�� ��ġ�� �ʴ� ��Ȳ���� �����̹Ƿ� del����.
			else if (Table[i][j] == Table[i-1][j - 1] + a && Table[i-1][j - 1] + a == Table[i - 1][j] + del_cost) {
				OP[0][count] = 'd';
				SR[0][count] = SS[i - 1];
				TR[0][count] = '*';
				i--;
				count++;
			}
			//sub�� ins�� ���� ���� del���� ������Ȳ.  sub�� ��ġ�� �ʴ� ��Ȳ���� �����̹Ƿ� ins����.
			else if (Table[i][j] == Table[i - 1][j - 1] + a && Table[i - 1][j - 1] + a == Table[i][j-1] + ins_cost) {
				OP[0][count] = 'i';
				SR[0][count] = '*';
				TR[0][count] = TS[j - 1];
				j--;
				count++;
			}
			//�´� ���� ��Ȳ
			else if (Table[i-1][j]+del_cost == Table[i][j - 1] + ins_cost && Table[i - 1][j - 1] + a == Table[i][j - 1] + ins_cost) {
				//cost �� �� ����
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
	//���� backtracing�� ����̹Ƿ� ����� ���� �迭�� �Ųٷ� �����´�.
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
	//�Ҵ� �� ���� ���� �޸𸮴� null������ ����.
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

//a�� ins_cost, b�� del_cost, c�� substitution, ins_cost<=del_cost�� ins����, ins_cost>del_cost�� del����, sub�� �Ѵٺ��� �۾ƾ� ����.
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
