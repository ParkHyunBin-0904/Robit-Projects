with open("memo.txt", "w",
           encoding="utf-8") as file:
    file.write("첫줄\n")
with open("memo.txt", "r",
           encoding="utf-8") as file:
    text = file.read()
print(text)

with open("result.csv","w",newline = "", encoding = "utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name","score"])

    writer.writeheader()
    writer.writerows(rows)
    writer.writerow(["name","score"])

with open("class.json",encoding = "utf-8") as file:
    date = json.load(file)

date["students"][0]["score"] = 90


