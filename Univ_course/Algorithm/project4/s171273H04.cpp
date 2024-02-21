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
	//closestPairDC를 진행하기 전 Xid 배열을 sort한다. 이때 mergesort를 이용한다.
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
	//main에서 sortXid함수를 사용한 후 파라미터를 받았으므로 이미 sort된 배열이다.

	//모든 점의 개수<=THR이면 Brute force사용
	if (R - L + 1 <= THR) {
		cd = closestPairBF(L, R, pt1, pt2, X, Y, Xid, Yid, TMP, THR);
		return cd;
	}
	//모든 점의 개수>THR이면 D&C알고리즘 사용하여 구현
	else {
		M = (L + R) / 2;
		//각각 이전 단계의 point를 저장한다.
		dL = closestPairDC(L, M, pt1, pt2, X, Y, Xid, Yid, TMP, THR);
		p1 = *pt1;
		p2 = *pt2;
		//각각 구하는 이유는 더 작은 distance였던 point를 반환하기 위해
		dR = closestPairDC(M + 1, R, pt1, pt2, X, Y, Xid, Yid, TMP, THR);
		p3 = *pt1;
		p4 = *pt2;
		merge2(L, M, R, Y, Yid, TMP);
		//여기서 더 작은 distance였던 point를 다시 지정
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
		//밑의 if경우는 THR이 1이거나 point가 하나여서 거리를 구하지 못한 경우
		if (dLR == DBL_MAX) {
			cd = sqrt((Y[p1] - Y[p3]) * (Y[p1] - Y[p3]) + (X[p1] - X[p3]) * (X[p1] - X[p3]));
			*pt1 = p3;
			*pt2 = p2;
			return cd;
		}
		//그 외 경우
		else {
			for (unsigned i = L; i <= R; i++) {
				if (X[Yid[i]] >= midL) {
					if (X[Yid[i]] <= midR) {
						//middle area의 point를 TMP배열에 저장.
						TMP[k] = Yid[i];
						k++;
					}
				}
			}
			//middle area에 포함되는 point가 없는 경우
			if (k == 0) {
				cd = dLR;
				return cd;
			}
		}
		//count는 middle area에서 구한 distance가 dLR보다 작지 않은 경우 예외 상황을 제어하기 위해
		int count = 0;
		double dij;
		//distanc구하는 과정
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
	//THR이 1이거나 partition진행 후 부득이하게 point가 하나만 남는 경우, 거리를 구할 수 없으므로 distance를 limit으로 지정
	if (R - L == 0) {
		cd = DBL_MAX;
		*pt1 = L;
		*pt2 = R;
		Yid[L] = Xid[L];
		Yid[R] = Xid[R];
		return cd;
	}
	else {
		//Yid 배열 복사
		for (unsigned e = L; e <= R; e++) {
			Yid[e] = Xid[e];
		}
		//Yid sort
		Yid = SelectionSort(L, R, Y, Yid);
		//거리 구하기
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
	//selection sort하기 위한 for문
	for (unsigned i = L; i < R; i++) {
		//배열의 i 값을 min으로 임시 지정
		min = i;
		//i+1부터 비교를 진행하여 제일 작은 값을 선택 후 교환
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