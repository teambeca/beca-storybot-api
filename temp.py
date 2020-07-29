with open("requirements.txt", "r", encoding="utf-8") as text_file:
    raw_text = text_file.read()
    text_file.close()

raw_text = raw_text.splitlines()

for x in range(len(raw_text)):
    temp = raw_text[x].split("==")
    raw_text[x] = temp[0] + "==" + temp[1]

with open("temp.txt", "w") as text_file:
    for t in raw_text:
        text_file.write(t + "\n")
