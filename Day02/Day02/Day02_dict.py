import csv
import json

# 정상 데이터와 점수를 저장할 리스트
clean = []
scores = []

# students.csv 파일 열기
try:
    with open("students.csv", "r", encoding="utf-8") as file:

        # DictReader 사용
        # 첫 번째 행(name, score)을 자동으로 제목으로 인식한다.
        reader = csv.DictReader(file)

        # 한 줄씩 읽기
        for row in reader:

            # 컬럼 이름으로 값 가져오기
            name = row["name"]
            score_text = row["score"]

            # 문자열을 정수로 변환
            try:
                score = int(score_text)

            # 숫자가 아니면 오류 출력 후 다음 학생 검사
            except ValueError:
                print(f"{name} : 숫자로 변환 실패 (값 : {score_text})")
                continue

            # 점수 범위 검사
            if score < 0 or score > 100:
                print(f"{name} : 허용범위 초과 (값 : {score})")
                continue

            # 정상 데이터 저장
            clean.append({
                "name": name,
                "score": score
            })

            # 통계 계산을 위한 점수 저장
            scores.append(score)

# students.csv가 없을 경우
except FileNotFoundError:
    print("students.csv 파일을 찾을 수 없습니다.")
    exit()

# 정상 학생만 clean_students.csv 저장
with open("clean_students.csv", "w", newline="", encoding="utf-8") as file:

    # DictWriter 생성
    writer = csv.DictWriter(file, fieldnames=["name", "score"])

    # 헤더(name,score) 작성
    writer.writeheader()

    # 정상 학생 저장
    for row in clean:
        writer.writerow(row)

# 통계 계산
if len(scores) > 0:
    count = len(scores)
    average = sum(scores) / count
    high = max(scores)
else:
    count = 0
    average = 0
    high = 0

# JSON으로 저장할 딕셔너리 생성
summary = {
    "count": count,
    "average": average,
    "max": high
}

# summary.json 저장
with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=4)

print("프로그램이 정상적으로 완료되었습니다.")