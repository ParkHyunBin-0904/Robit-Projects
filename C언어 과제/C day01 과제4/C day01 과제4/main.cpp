#include<stdio.h>

int main(void) {
	// 첫 문구와 예시 출력
	printf("Input Arithmetic Operation\n");
	printf("ex)      3.4 * 8.5\n");
	printf("         2.9 - 5.4\n");
	printf("         3.9 * 8.0\n");
	printf("         3.9 ^ 8\n\n");
	printf("input: ");

	double num1, num2 = 0;
	char op;
	double result = 0;
	// 입력 받기
	scanf_s("%lf %c %lf", &num1, &op,1, &num2);

	// 덧셈
    if (op == '+') {
		result = num1 + num2;
		printf("% .2f %c %.2f = %.2f\n", num1, op, num2, result);
	}
	// 뺄셈
	else if (op == '-') {
		result = num1 - num2;
		printf("% .2f %c %.2f = %.2f\n", num1, op, num2, result);
	}
	// 곱셈
	else if (op == '*') {
		result = num1 * num2;
		printf("% .2f %c %.2f = %.2f\n", num1, op, num2, result);
	}
	// 나눗셈
	else if (op == '/') {
		result = num1 / num2;
		printf("% .2f %c %.2f = %.2f\n", num1, op, num2, result);
	}
	// 거듭제곱
	else if (op == '^') {
		result = 1.0; // 곱셈하기 위해 0 -> 1로 바꿔줌
		for (int i = 0; i < (int)num2; i++) {
			result *= num1;
		}
		printf("% .2f %c %.2f = %.2f\n", num1, op, num2, result);
	}
	printf("계속하려면 아무 키나 누르십시오 . . .");

	return 0;
}