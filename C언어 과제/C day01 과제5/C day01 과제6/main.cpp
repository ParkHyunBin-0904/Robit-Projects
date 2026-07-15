#include<stdio.h>

int main(void) {

	printf("값을 입력하세요. ");

	// 입력값
	int num;
	scanf_s("%d", &num);

	// 앞 공백
	for (int i = 1; i <= num; i++) {
		for (int k = num - i; k >= 1; k--) {
			printf(" ");
		}
		for (int j = 1; j <= i*2-1; j++){
			// 마지막줄
			if (i == num) {
				printf("*");
			}
			// 마지막줄 제외 나머지
			else {
				// 앞과 끝 별
				if (j == 1 || j == i * 2 - 1) {
					printf("*");
				}
				// 별 사이 공백
				else {
					printf(" ");
				}
			}
		}
		printf("\n");
	}
	
	return 0;
}