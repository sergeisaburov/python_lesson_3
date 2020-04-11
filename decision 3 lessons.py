print('3 Урок 1 Задание: методами строк очистить текст от знаков препинания.')
handle = open(r"D:\pytnon\text.txt")
rasskaz_without = handle.read()
rasskaz_without = rasskaz_without.replace(".", "")
rasskaz_without = rasskaz_without.replace(",", "")
rasskaz_without = rasskaz_without.replace("—", "")
rasskaz_without = rasskaz_without.replace("«", "")
rasskaz_without = rasskaz_without.replace("»", "")
rasskaz_without = rasskaz_without.replace("?", "")
rasskaz_without = rasskaz_without.replace("!", "")
print(rasskaz_without)
handle.close()
print('3 Урок 1 Задание ВЫПОЛНЕНО')
# сформировать list со словами (split);-----------------------------------------------
print('3 Урок 2 Задание: сформировать list со словами (split).')
handle = open(r"D:\pytnon\text.txt")
rasskaz = handle.read()
rasskaz_razd = rasskaz.split()
print(rasskaz_razd)
print('3 Урок 2 Задание ВЫПОЛНЕНО')
# # привести все слова к нижнему регистру (map)----------------------------------------------------
print('3 Урок 3 Задание: привести все слова к нижнему регистру (map).')
handle = open(r"D:\pytnon\text.txt")
rasskaz = handle.read()
low_reg = rasskaz.lower()
print(low_reg)
print('3 Урок 3 Задание ВЫПОЛНЕНО')
# получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;---------------------------------
print('3 Урок 4 Задание: получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте.')
rasskaz_razd1 = rasskaz_without.split()
from collections import Counter
# list1=[rasskaz_razd]
counts = Counter(rasskaz_razd1)
slovar=dict(counts)
print(slovar)
print('3 Урок 4 Задание ВЫПОЛНЕНО')
# вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
print('3 Урок 5 Задание: вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')



print('3 Урок 5 Задание ВЫПОЛНЕНО')
