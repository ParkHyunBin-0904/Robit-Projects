#include<stdio.h>

int main(void) {

	int n; 
	scanf_s("%d", &n);    // n 입력

	int F[100];           // 수 저장할 배열
	F[0] = 0;            
	F[1] = 1;
	
	for (int i = 2; i <= n; i++) {      // n번째까지 반복
		F[i] = F[i - 1] + F[i - 2];
	}

	printf("%d", F[n-1]);         // 0번째부터 시작하므로 n-1번째 구함

	return 0;

}