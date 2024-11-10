import json
# TODO решите задачу
#Объявляем функцию с именем task, которая возвращает значение типа float.
def task() -> float:
    #Cоздаем строку file, в которой хранится имя файла "input.json", из которого будут загружены данные.
    file = "input.json"
    #Открываем файл с именем, хранящимся в переменной file. Файл присваивается переменной a. Используем with, чтобы файл автоматически закрылс после завершения блока кода.
    with open(file) as a:
        #Загружаем содержимое файла a в формате JSON и преобразуем его в структуры данных Python в переменную json_data.
        json_data = json.load(a)
    #Создаем генератор списка с помощью выражения [item["score"] * item["weight"] for item in json_data], которое проходит по каждому элементу item в json_data.Для каждого элемента выбираем значения по ключам "score" и "weight" и перемножаем.
    total_sum = sum([item["score"] * item["weight"] for item in json_data])
    #Возвращаем значение total_sum, округленное до трех знаков после запятой с помощью функции round().
    return round(total_sum, 3)

print(task())
