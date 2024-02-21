#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <float.h>
#pragma warning(disable: 4819)

unsigned* SelectionSort(unsigned L, unsigned R, double* Y, unsigned* Yid);
double closestPairBF(unsigned L, unsigned R, unsigned* pt1, unsigned* pt2, double* X, double* Y, unsigned* Xid, unsigned* Yid, unsigned* TMP, unsigned THR);
void mergesort2(unsigned L, unsigned R, double* X, unsigned* Xid, unsigned* TMP);
void merge2(unsigned L, unsigned M, unsigned R, double* X, unsigned* Xid, unsigned* TMP);


void sortXid(double* X, unsigned* Xid, unsigned* TMP, unsigned N) {
	//closestPairDC�� �����ϱ� �� Xid �迭�� sort�Ѵ�. �̶� mergesort�� �̿��Ѵ�.
	mergesort2(0, N - 1, X, Xid, TMP);
}

double closestPairDC(unsigned L, unsigned R, unsigned* pt1, unsigned* pt2, double* X, double* Y, unsigned* Xid, unsigned* Yid, unsigned* TMP, unsigned THR) {

	//distance
	double cd;
	//for partition
	unsigned M;
	//distance
	double dL;
	double dR;
	double dLR;
	//for middle area
	double Xmid;
	double midL;
	double midR;
	//for point
	unsigned p1, p2, p3, p4;
	//main���� sortXid�Լ��� ����� �� �Ķ���͸� �޾����Ƿ� �̹� sort�� �迭�̴�.

	//��� ���� ����<=THR�̸� Brute force���
	if (R - L + 1 <= THR) {
		cd = closestPairBF(L, R, pt1, pt2, X, Y, Xid, Yid, TMP, THR);
		return cd;
	}
	//��� ���� ����>THR�̸� D&C�˰��� ����Ͽ� ����
	else {
		M = (L + R) / 2;
		//���� ���� �ܰ��� point�� �����Ѵ�.
		dL = closestPairDC(L, M, pt1, pt2, X, Y, Xid, Yid, TMP, THR);
		p1 = *pt1;
		p2 = *pt2;
		//���� ���ϴ� ������ �� ���� distance���� point�� ��ȯ�ϱ� ����
		dR = closestPairDC(M + 1, R, pt1, pt2, X, Y, Xid, Yid, TMP, THR);
		p3 = *pt1;
		p4 = *pt2;
		merge2(L, M, R, Y, Yid, TMP);
		//���⼭ �� ���� distance���� point�� �ٽ� ����
		if (dL > dR) {
			dLR = dR;
			*pt1 = p3;
			*pt2 = p4;
		}
		else {
			dLR = dL;
			*pt1 = p1;
			*pt2 = p2;
		}
		//middle area
		Xmid = (X[Xid[M]] + X[Xid[M + 1]]) / 2;
		midL = Xmid - dLR;
		midR = Xmid + dLR;
		unsigned k = 0;
		//���� if���� THR�� 1�̰ų� point�� �ϳ����� �Ÿ��� ������ ���� ���
		if (dLR == DBL_MAX) {
			cd = sqrt((Y[p1] - Y[p3]) * (Y[p1] - Y[p3]) + (X[p1] - X[p3]) * (X[p1] - X[p3]));
			*pt1 = p3;
			*pt2 = p2;
			return cd;
		}
		//�� �� ���
		else {
			for (unsigned i = L; i <= R; i++) {
				if (X[Yid[i]] >= midL) {
					if (X[Yid[i]] <= midR) {
						//middle area�� point�� TMP�迭�� ����.
						TMP[k] = Yid[i];
						k++;
					}
				}
			}
			//middle area�� ���ԵǴ� point�� ���� ���
			if (k == 0) {
				cd = dLR;
				return cd;
			}
		}
		//count�� middle area���� ���� distance�� dLR���� ���� ���� ��� ���� ��Ȳ�� �����ϱ� ����
		int count = 0;
		double dij;
		//distanc���ϴ� ����
		for (unsigned i = 0; i < k-1; i++) {
			for (unsigned j = i + 1; j <= k-1; j++) {
				if (Y[TMP[i]] - Y[TMP[j]] >= dLR) break;
				dij = sqrt((Y[TMP[i]] - Y[TMP[j]]) * (Y[TMP[i]] - Y[TMP[j]]) + (X[TMP[i]] - X[TMP[j]]) * (X[TMP[i]] - X[TMP[j]]));
				if (dij < dLR) {
					dLR = dij;
					p1 = TMP[i];
					p2 = TMP[j];
					count = count + 1;
				}
			}
		}
		if (count > 0) {
			*pt1 = p1;
			*pt2 = p2;
		}
		cd = dLR;
	}
	return cd;
}

double closestPairBF(unsigned L, unsigned R, unsigned* pt1, unsigned* pt2, double* X, double* Y, unsigned* Xid, unsigned* Yid, unsigned* TMP, unsigned THR) {

	//distance

	double cd;
	double d = DBL_MAX;
	unsigned p1 = 0, p2 = 0;
	//THR�� 1�̰ų� partition���� �� �ε����ϰ� point�� �ϳ��� ���� ���, �Ÿ��� ���� �� �����Ƿ� distance�� limit���� ����
	if (R - L == 0) {
		cd = DBL_MAX;
		*pt1 = L;
		*pt2 = R;
		Yid[L] = Xid[L];
		Yid[R] = Xid[R];
		return cd;
	}
	else {
		//Yid �迭 ����
		for (unsigned e = L; e <= R; e++) {
			Yid[e] = Xid[e];
		}
		//Yid sort
		Yid = SelectionSort(L, R, Y, Yid);
		//�Ÿ� ���ϱ�
		for (unsigned i = L; i < R; i++) {
			for (unsigned j = i + 1; j <= R; j++) {
				cd = sqrt((Y[Yid[i]] - Y[Yid[j]]) * (Y[Yid[i]] - Y[Yid[j]]) + (X[Yid[i]] - X[Yid[j]]) * (X[Yid[i]] - X[Yid[j]]));
				if (d > cd) {
					d = cd;
					p1 = Yid[i];
					p2 = Yid[j];
				}
			}
		}
		cd = d;
		*pt1 = p1;
		*pt2 = p2;
		return cd;
	}
}

unsigned* SelectionSort(unsigned L, unsigned R, double* Y, unsigned* Yid) {
	unsigned min;
	unsigned tmp;
	//selection sort�ϱ� ���� for��
	for (unsigned i = L; i < R; i++) {
		//�迭�� i ���� min���� �ӽ� ����
		min = i;
		//i+1���� �񱳸� �����Ͽ� ���� ���� ���� ���� �� ��ȯ
		for (unsigned j = i + 1; j <= R; j++) {
			if (Y[Yid[j]] < Y[Yid[min]]) {
				min = j;
			}
		}
		tmp = Yid[i];
		Yid[i] = Yid[min];
		Yid[min] = tmp;
	}
	return Yid;
}

void mergesort2(unsigned L, unsigned R, double* X, unsigned* Xid, unsigned* TMP) {
	unsigned M;
	if (L < R) {
		M = (L + R) / 2;
		mergesort2(L, M, X, Xid, TMP);
		mergesort2(M + 1, R, X, Xid, TMP);
		merge2(L, M, R, X, Xid, TMP);
	}
}

void  merge2(unsigned L, unsigned M, unsigned R, double* X, unsigned* Xid, unsigned* TMP) {

	unsigned i, j, k;
	i = L, j = M + 1, k = L;
	while (i <= M && j <= R) {
		if (X[Xid[i]] < X[Xid[j]]) {
			TMP[k] = Xid[i];
			i++;
			k++;
		}
		else {
			TMP[k] = Xid[j];
			j++;
			k++;
		}
	}
	if (i > M) {
		while (j <= R) {
			TMP[k] = Xid[j];
			j++;
			k++;
		}
	}
	else {
		while (i <= M) {
			TMP[k] = Xid[i];
			i++;
			k++;
		}
	}
	for (unsigned e = L; e <= R; e++) {
		Xid[e] = TMP[e];
	}
}