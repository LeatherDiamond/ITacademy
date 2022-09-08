# Request of necessary data from user.
input_height = float(input("Введите ваш рост (см):"))
input_weight = float(input("Введите вашу массу тела (кг):"))
input_gender = str(input("Введите ваш пол (мужской, женский):"))
input_age = float(input("Введите ваш возраст (полное кол-во лет):"))
# BMI calculation and printing of the result.
BMI = round(input_weight/(input_height**2/10000))
print("Ваш индекс массы тела (кг/м^2):" + str(BMI))
# Printing of the scale.
list1 = '16=======================40'
list2 = list1[0:(BMI-15)] + "|" + list1[(BMI-14):]
print(list2)
# Printing recomendations according to gender of user.
if input_gender == str('женский') and BMI > 16 and BMI < 19:
    print('Дефицит массы тела. Потребляйте больше калорий.')
elif input_gender == str('женский') and BMI > 19 and BMI < 25:
    print('У вас нормальная масса тела. Поддерживайте баланс питания.')
elif input_gender == str('женский') and BMI > 25:
    print('У вас избыточная масса тела. Усильте физические нагрузки и соблюдайте диету, которую назначит специалист.')
elif input_gender == str('мужской') and BMI > 16 and BMI < 25:
    print('У вас нормальная масса тела. Поддерживайте баланс питания.')
elif input_gender == str('мужской') and BMI > 25 and BMI < 30:
    print('У вас избыточная масса тела. Усильте физические нагрузки и обратите внимание на питание.')
elif input_gender == str('мужской') and BMI > 30:
    print('У вас ожирение. Обратиетьс к специалисту для составления персональной диеты и усильте физическую активность.')
# Printing recomendations according to age of user.
if input_gender == str('женский') and input_age > 19 and input_age < 25 and BMI == 20:
    print('Ваш ИМТ соответствует вашему возрасту. Поддерживайте баланс питания и физической активности.')
elif input_gender == str('женский') and input_age > 25 and input_age < 35 and BMI == 24:
    print('Ваш ИМТ соответствует вашему возрасту. Поддерживайте баланс питания и физической активности.')
elif input_gender == str('женский') and input_age > 35 and input_age < 55 and BMI == 25:
    print('Ваш ИМТ соответствует вашему возрасту. Поддерживайте баланс питания и физической активности.')
elif input_gender == str('мужской') and input_age > 19 and input_age < 25 and BMI == 22:
    print('Ваш ИМТ соответствует вашему возрасту. Поддерживайте баланс питания и физической активности.')
elif input_gender == str('мужской') and input_age > 25 and input_age < 35 and BMI == 25:
    print('Ваш ИМТ соответствует вашему возрасту. Поддерживайте баланс питания и физической активности.')
elif input_gender == str('мужской') and input_age > 35 and input_age < 55 and BMI == 26:
    print('Ваш ИМТ соответствует вашему возрасту. Поддерживайте баланс питания и физической активности.')
print('Данный калькулятор дает лишь советы исходя из вашего ИМТ и возраста, поэтому для получения квалифицированной \
консультации, пожалуйста, обратитесь к сертифицированным специалистам. ')