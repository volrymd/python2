# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import sqrt
s = int(input('Введите cумму двух чисел: '))
p = int(input('Введите cумму произведение чисел: '))
x = (s-int((sqrt(s**2-4*p))))//2
y = (s+int((sqrt(s**2-4*p))))//2
print(x, y)
