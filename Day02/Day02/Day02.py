import csv
import json

clean = []
scores = []

try:
    # students.csv 파일 열기
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # 첫 줄(header) 건너뛰기
        next(reader)

        # 한 줄씩 읽기
        for row in reader:

            name = row["name"]
            score_text = row[1]

            # 숫자로 변환
            try:
                score = int(score_text)
            except ValueError:
                print(f"{name} : 숫자로 변환 실패")
                continue

            # 범위 검사
            if score < 0 or score > 100:
                print(f"{name} : 허용범위 초과")
                continue

            # 정상 데이터 저장
            clean.append([name, score])
            scores.append(score)

except FileNotFoundError:
    print("students.csv 파일이 없습니다.")
    exit()

# 정상 데이터 CSV 저장
with open("clean_students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # 제목 저장
    writer.writerow(["name", "score"])

    # 학생 정보 저장
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

summary = {
    "count": count,
    "average": average,
    "max": high
}

# JSON 저장
with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=4)   # 한글 깨지지 않게 

print("프로그램이 정상적으로 완료되었습니다.")