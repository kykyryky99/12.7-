kolichestvo_biletov = int(input())
count = 0
summa = 0

for bilet in range(1, kolichestvo_biletov+1):
    count += 1
    vozrast_bilet = int(input(f'Введите возраст человека покупающего {bilet}-й билет '))
    if vozrast_bilet < 18:
        print("Бесплатный билет")
    elif 18 <= vozrast_bilet < 25:
        print("Стоимость билета 990 руб.")
        summa += 990
    elif vozrast_bilet >= 25:
        print("Стоимость билета 1390 руб.")
        summa += 1390
if count > 3:
    summa_10 = int(summa * 0.9)
    skidka = summa - summa_10
    print(f"Общая стоимоть билетов: {summa_10} руб.,"
          f" ваша скидка: {skidka} руб")
else:
    print(f"Общая стоимоть билетов составила: {summa}")
