#include<stdio.h>

int main(void) {

	printf("값을 입력하세요.");

	// 수 입력
	int num;
	scanf_s("%d", &num);
	// 위에서부터 중앙까지 별
	for (int i = 1; i <= num; i++) {
		// 왼쪽 별
		for (int j = 1;j <= i; j++) {
			printf("*");
		}
		// 중간 공백
		for (int k = 1; k <= num - i; k++) {
			printf("  ");
		}
		// 오른쪽 별
		for (int l = 1;l <= i; l++) {
			printf("*");
		}
		// 줄바꿈
		printf("\n");
	}
	// 위에서부터 중앙 아랫쪽 별
	for (int i = num - 1; i >= 1; i--) {
		// 왼쪽 별
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		// 중간 공백
		for (int k = 1; k <= num - i; k++) {
			printf("  ");
		}
		// 오른쪽 별
		for (int l = 1;l <= i; l++) {
			printf("*");
		}
		// 줄바꿈
		printf("\n");
	}
}
