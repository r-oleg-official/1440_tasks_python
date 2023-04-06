# 1.1. Вывести на одной строке числа 31, 18 и 79 с одним пробелом между ними. Текст '31 18 79' не использовать.

# Easter egg. Операция конкатенации

# Ввод данных. Присвоение значений переменным вариант 1.
a = 31
b = 18
c = 79
# Ввод данных. Присвоение значений переменным, используя список вариант 2.
# a, b, c = [31, 18, 79]

# Answer v.1.
d = str(a)
e = str(b)
f = str(c)
result = d + " " + e + " " + f
print("Answer 1: ", result)

# Answer v.2.
result = str(a) + " " + str(b) + " " + str(c)
print("Answer 2: ", result)

# Answer v.3.
print("Answer 3: ", str(a) + " " + str(b) + " " + str(c))


# Answer v.4.
# Используя функцию concatenate()
def concatenate(x: int, y: int, z: int) -> str:
    return str(x) + " " + str(y) + " " + str(z)


print("Answer 4: ", concatenate(a, b, c))
