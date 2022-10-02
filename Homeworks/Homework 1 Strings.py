text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

"""Step 1 - Printing quantity of symbols."""
print("Шаг1 - Количество символов - " + str(len (text)) + '.')

"""Step 2 - Expaded string."""
print("Шаг2 - Развернутая строка - " + text[::-1] )

"""Step 3 - Every word from capital letter."""
print("Шаг3 - Каждое слово с большой буквы - " + str.title(text))

"""Step 4 - Uppercase text."""
print("Шаг4 - Текст прописными буквами - " + str.upper(text))

"""Step 5 - Quantity of special symbols in the string"""
print("Шаг5 - Число вхождений 'нд', 'ам', 'о' в строку - " + str(text.count('нд')) + " раз 'нд'" ',\t' \
+ str(text.count('ам')) + " раза 'ам'" ',\t' + str(text.count('о')) + " раз 'о'" '.')

"""Step 6 - Personal exercises"""
print("Шаг6 - Собственные упражнения: а) Замена слова в предложении (2 способа)*, б) Вывод в консоли последних\
двух слов исходного предложения. ")
text1 = text[0:19] + 'Берлине' + text[26:]
print("Шаг 6а - " + text1)
print("Шаг 6а* - " + text.replace ('собака', 'кот'))
print("Шаг 6б - " + text[-14:-1])

"""Step 7 - reversed sentence"""
text2 = text.split()
text2_rev = list(reversed(text2))
print("Шаг7 - Развернутое предложение - " + str(text2_rev))

"""Step 8 - Printing of original string."""
print("Шаг8 - Вывод в консоль исходной строки - " + text)