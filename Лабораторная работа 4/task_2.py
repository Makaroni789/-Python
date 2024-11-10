# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f:
        #csv.DictReader(f) читает файл f и возвращает возвращает каждую строку файла в виде словаря, где заголовки CSV используются как ключи.
        lines = [line for line in csv.DictReader(f)]
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as f:
        #json.dump(lines, f, indent=4) записывает список словарей lines в файл f в формате JSON, с отступами в 4 пробела.
        json.dump(lines, f, indent=4)

if __name__ == '__main__':
    #Проверяет, был ли файл запущен как основная программа. Если это так, выполняется код внутри блока.
    task()

    with open(OUTPUT_FILENAME) as output_file:
        #Проходим по каждой строке в выходном файле.
        for line in output_file:
            #print(line, end="") выводит строку на экран без добавления дополнительной новой строки.
            print(line, end="")
