import csv
import operator

with open('books.csv',  encoding = 'windows-1251') as file:  # открытие файла books.csv для чтения
    reader = csv.reader(file, delimiter = ";")  # чтение файла
    data = list(reader)
    element_count = len([item for item in data if len(item[1]) - 30 > 0])  # поиск элементов списка, длинна которых больше 30 символов
    print("Всего записей: %d" %len(data))
    print("количество записей, длинна которых более 30: %d" %element_count)
    search=input("Введите имя и фамилию  автора: ")  # ввод ФИО автора
    data_auth = [item for item in data if item[3].lower() == search.lower()]  # поиск всех записей с этим автором (не зависимо от ввода, поиск будет осуществляться в нижнем регистре)
    element_count = [item for item in data_auth if len(item[7]) < 150]  # из выше отобранного списка находим те книги, стоимость которых менее 150 рублей
    if len(element_count) >= 1:
        print('Книги автора %s до 150 рублей: ' %search)
        for ans in element_count:                               # Построчный вывод элементов спсика
            print('\t - %s' %ans[1])
    else:
        print('Книги автора %s не найдены' %search)
    tags_array = []  # пустой список, в который мы будем записывать теги
    for i in range(len(data)):                  # для каждой строки таблицы
        tags = list(data[i][12].split('#'))     # в 12-м столбце находим тэги разделенные '#'
        for tag in tags:
            if not (tag.strip() in tags_array):  # если тега нет в нашем списке, то мы его туда записываем
                tags_array.append(tag.strip())
    with open('tags.txt', 'w', encoding = 'utf-8') as f: # открытие файла tags.txt для записи
        for i in tags_array:                             # записываем все теги в файл
            f.writelines(i + '\n')
with open('books.csv',  encoding = 'windows-1251') as file:  # открытие файла books.csv для чтения
    reader = csv.reader(file, delimiter = ";")  # чтение файла
    sortedlist = sorted(reader, key=operator.itemgetter(9), reverse=True)  # сортировка таблицы по количеству выданных книг
    print('Самые популярные книги:')
    for i in range(1,21):  # вывод 20 самых популярных книг
        print('\t %d %s' %(i, sortedlist[i][1]))

    with open('result.txt', 'w', encoding = 'utf-8') as res:  # открытие файла result.txt для записи
        for i in range(1,21):                                 # запись результата в файл
            res.writelines('%s. %s - %s \n' %(sortedlist[i][3], sortedlist[i][1], sortedlist[i][6]))
print('Все теги представлены в файле: tags.txt')
print('Ссылки для 20 записей представлены в файле: result.txt')