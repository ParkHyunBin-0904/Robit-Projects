#include<stdio.h>

int main(void) {

	int n, r;
	// n r 입력 받기
	printf("n과 r을 입력하세요: ");
	scanf_s("%d %d", &n, &r);
	// 변수들 결과 커질 수 있으므로 int 대신 long long 사용
	long long P = 1;
	long long h = 1;
	long long C = 1;
	long long H = 1;
	// 순열
	for (int i = n-r+1; i <= n; i++) {
		P *= i;
	}
	// 중복순열
	for (int i = 1; i <= r; i++) {
		h *= n;
	}
	// 조합
	C = P;
	for (int i = 1; i <= r; i++) {
		C /= i;
	}
	// 중복조합
	long long up = 1;
	long long down = 1;
	for (int i = 1; i <= n+r-1; i++) {
		up *= i;
	}
	for (int i = 1; i <= n-1; i++) {
		down *= i;
	}
	for (int i = 1; i <= r; i++) {
		down *= i;
	}
	H = up / down;

	// 결과 출력 - 결과 커질 수 있으므로 %d -> %lld 사용
	printf("순열 : %lld\n", P);
	printf("중복순열 : %lld\n", h);
	printf("조합 : %lld\n", C);
	printf("중복조합 : %lld\n", H);
}