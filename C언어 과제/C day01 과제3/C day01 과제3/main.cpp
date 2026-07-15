#include<stdio.h>

int main(void) {
	// 년도 입력
	int year;
	printf("년도를 입력하세요 : ");
	scanf_s("%d", &year);
	// 4의 배수 일때
	if (year % 4 == 0) {
		// 100으로 나눠질 때
		if (year % 100 == 0) {
			// 400으로 나눠질 때
			if (year % 400 == 0) {
				printf("윤년");
			}
			else {
				printf("윤년이 아닙니다");
			}
		}
		else {
			printf("윤년");
		}
	}
}