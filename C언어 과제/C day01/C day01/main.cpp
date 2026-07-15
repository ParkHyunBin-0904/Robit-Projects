#include<stdio.h>

int main(void) {

	float sum = 0; 
	float max = 0;
	float min;

	for (int i = 1; i <= 5; i++) {           // 5번 반복 
		printf("%d 번째 실수를 입력하시오. ", i);
		float num;
		scanf_s("%f", &num);                 // 숫자 입력
		sum += num;                          // 총합에 숫자 더하기 
		if (i == 1) {                        // 최대 최소 최초 저장
			max = num;
			min = num;
		}
		else if (num > max) {                // 최댓값
			max = num;
		}
		else if (num < min) {                // 최솟값
			min = num;
		}
	}

	printf("---- 결과 ----\n");
	printf("평균은 %f 입니다.\n", sum/5);
	printf("최댓값은 %f 입니다.\n", max);
	printf("최솟값은 %f 입니다.\n", min);
}

