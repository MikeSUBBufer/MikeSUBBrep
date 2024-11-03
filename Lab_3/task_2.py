# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(str_1, str_2, separate = ','):
    mn_1 = set(str_1.split(str(separate)))
    mn_2 = set(str_2.split(str(separate)))

    new_mn = mn_1.intersection(mn_2)

    new_list = (list(new_mn))
    new_list.sort()

    return new_list

print(find_common_participants(participants_first_group,participants_second_group, separate="|"))