import re, csv


#Task 1
with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#Task 2
with open('task2.html', 'r', encoding='utf-8') as file:
    html = file.read()

#Task 3
with open('task3.txt', 'r', encoding='utf-8') as file:
    data = file.read().split()

ids = [st for st in data if re.fullmatch(r'\d+', st)] #любая цифра
fam = [st for st in data if re.fullmatch(r'[A-Z][a-zA-Z]+', st)]
emails = [st for st in data if re.fullmatch(r'\S+@\S+', st)] #юольшая s любой не пробедьный символ
date = [st for st in data if re.fullmatch(r'\d{4}-\d{2}-\d{2}', st)]
web = [st for st in data if re.fullmatch(r'https?://\S+|www\.\S+', st)] #ы? 0 или 1 раз встречается

rows = [[ids[i], fam[i], emails[i], date[i], web[i]] for i in range(len(ids))]

if __name__ == '__main__':
    print(re.findall(r'\bс[а-яё]+\b', text, flags=re.I))  #\b - граница слова, flags=re.I -игнорирование регистра
    print(re.findall(r'\bи\s+([а-яё]+)\b', text, flags=re.I))  #\s+ более одного пробела после и или знак табуляции

    print(re.findall(r"font-family\s*:\s*'([^']+)'", html)) #одинарная кавычка (начало названия шрифта), [^'] - любой символ, КРОМЕ (^) одинарной кавычки

    with open('task3_solving.csv','w', encoding='utf-8', newline='') as f:
        table = csv.writer(f)
        table.writerow(['ID','Фамилия','Email','Дата','Сайт'])
        table.writerows(rows)