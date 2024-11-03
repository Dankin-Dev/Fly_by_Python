# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=","):
    participants_list1 = first.split(separator)
    participants_list2 = second.split(separator)
    common = list(set(participants_list1).intersection(participants_list2))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", result)