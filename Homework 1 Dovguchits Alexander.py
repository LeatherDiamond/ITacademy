text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print("Шаг1 - Количество символов - " + str(len (text)) + '.')

print("Шаг2 - Развернутая строка - " + text[::-1] )

print("Шаг3 - Каждое слово с большой буквы - " + str.title(text))

print("Шаг4 - Текст прописными буквами - " + str.upper(text))

print("Шаг5 - Число вхождений 'нд', 'ам', 'о' в строку - " + str(text.count('нд')) + " раз 'нд'" ',\t' \
+ str(text.count('ам')) + " раза 'ам'" ',\t' + str(text.count('о')) + " раз 'о'" '.')

print("Шаг6 - Собственные упражнения: а) Замена слова в предложении (2 способа)*, б) Вывод в консоли последних\
двух слов исходного предложения. ")
text1 = text[0:19] + 'Берлине' + text[26:]
print("Шаг 6а - " + text1)
print("Шаг 6а* - " + text.replace ('собака', 'кот'))
print("Шаг 6б - " + text[-14:-1])

text2 = text.split()
text2_rev = list(reversed(text2))
print("Шаг7 - Развернутое предложение - " + str(text2_rev))

print("Шаг8 - Вывод в консоль исходной строки - " + text)