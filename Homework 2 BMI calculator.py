h = float(input("Введите Ваш рост (см):"))
m = float(input("Введите Вашу массу тела (кг):"))
print("Индекс массы Вашего тела (кг/м^2):" + str(round(m/(h**2/10000))))