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
# # сформировать list со словами (split);-----------------------------------------------
print('3 Урок 2 Задание: сформировать list со словами (split).')
handle = open(r"D:\pytnon\text.txt")
rasskaz = handle.read()
rasskaz_razd = rasskaz.split()
print(rasskaz_razd)
print('3 Урок 2 Задание ВЫПОЛНЕНО')
# # # привести все слова к нижнему регистру (map)----------------------------------------------------
print('3 Урок 3 Задание: привести все слова к нижнему регистру (map).')
handle = open(r"D:\pytnon\text.txt")
rasskaz = handle.read()
low_reg = rasskaz.lower()
print(low_reg)
print('3 Урок 3 Задание ВЫПОЛНЕНО')
# # получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;---------------------------------
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
handle = open(r"D:\pytnon\text.txt")# открываем файл по адресу
rasskaz_without = handle.read() # читаем открытый файл
rasskaz_without = rasskaz_without.replace(".", "")  # из файла удаляем точки
rasskaz_without = rasskaz_without.replace(",", "")  # из файла удаляем запятые
rasskaz_without = rasskaz_without.replace("—", "")  # из файла удаляем —
rasskaz_without = rasskaz_without.replace("«", "")  # из файла удаляем «
rasskaz_without = rasskaz_without.replace("»", "")  # из файла удаляем »
rasskaz_without = rasskaz_without.replace("?", "")  # из файла удаляем ?
rasskaz_without = rasskaz_without.replace("!", "")  # из файла удаляем !
 # Закрываем файловый объект  handle (высвобождем ресурсы памяти), то есть закрываем открытый файл
# но текст из файла остается в переменной rasskaz_without
handle.close()
low_reg = rasskaz_without.lower()  # в переменной rasskaz_without есть слова с заглавными буквами, эти слова делаем все со строчными буквами
list_ = low_reg   # просто перекидываем  одну переменную
print(type(list_),list_)    # определяем тип переменной (это будет <class 'str'> ) и выводим переменную
list_ = list_.split()
print(type(list_),list_)    # определяем тип переменной (это будет <class 'list'> [ ) и выводим переменную
dict_ = {} # теперь можно например задать какой то пустой словарь
for word in list_: # потом пройтись циклом по списку слов:
# в цикле: БЕРЕМ СЛОВО и путем перебора считаем его количество в списке и записываем в словарь так:
# 'слово': количество , 'слово': количество , 'слово': количество
    dict_[word] = list_.count(word)
print(dict_)
print(type(dict_),dict_)    # определяем тип переменной (это будет <class 'dict'> { ) и выводим переменную
# СЛОВАРЬ превращаем в СПИСОК и записывается так:
# ('слово', количество) , ('слово', количество) , ('слово', количество)
list_d = list(dict_.items()) # СЛОВАРЬ превращаем в СПИСОК
print(list_d)  # выводим  СПИСОК
# СПИСОК сортируем по возрастанию, начиная с первого слова, которое всего одно в списке,
# далее второе слово,которое тоже всего одно в списке, слова по очереди, а по возратанию ставится их количество в тексте
list_d.sort(key=lambda i: i[1]) # сортируем по возрастанию
print(list_d)
list_d.sort(key=lambda i: i[1] , reverse=True) # сортируем по убыванию
print(list_d)
print(list_d[0:5]) # выводим первые пять элементов списка

# САМЫЙ понятный пример с count
print('Abracadabra'.count('a'))  # вернёт 4  (count входит  в  Abracadabra и считает количество а )

print('3 Урок 5 Задание ВЫПОЛНЕНО')
