# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    # Преобразуем строки в списки участников
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Находим общих участников
    common_participants = set(participants1) & set(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group)
print(common)