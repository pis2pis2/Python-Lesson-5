
number=int(input('Введите целое число от 1 до 1000: '))
def _get_dividers(number):
    """
    :param number: int from 1 to 1000
    :return: all dividers of this number
    """
    dividers = []
    for i in range(1, number + 1):
        if number % i == 0:
            dividers.append(i)
    return dividers
print("Все делители числа:")
print(_get_dividers(number))


def is_simple(number):
    """
    :param number: int figure
    :return: true or false depending if it is simple or not integer figure
    """

    divrs_list = _get_dividers(number)
    if (len(divrs_list) == 2) == True & ((1 in divrs_list) == True) & ((number in divrs_list) == True):
        return True
    else:
        return False
print("Простое ли это число?")
print(is_simple(number))

#
# def print_dividers(number):
#     divrs_list = _get_dividers(number)
#     print('Divider list of {}: {}\n'.format(number, divrs_list))
#
# def _get_all_simple_dividers(divs_list):
#     """
#     :param divs_list: all dividers list, integer number list
#     :return: only simple divider list
#     """
#     simple_dvrs = []
#     for i in range(0, len(divs_list)):
#         if is_simple(divs_list[i]):
#             simple_dvrs.append(divs_list[i])
#     return simple_dvrs
#
# # print(10%6)