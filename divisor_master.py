
number=int(input('Введите целое число от 1 до 1000: '))
if 1 <= number <= 1000:
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

    divrs_list = _get_dividers(number)
    def _get_all_simple_dividers(divrs_list):
        """
        :param divs_list: all dividers list, integer number list
        :return: only simple divider list
        """

        simple_dvrs = []
        for i in range(0, len(divrs_list)):
            if is_simple(divrs_list[i]):
                simple_dvrs.append(divrs_list[i])
        return simple_dvrs
    print('Все простые делители числа:')
    print(_get_all_simple_dividers(divrs_list))

    simple_dvrs = _get_all_simple_dividers(divrs_list)
    def max_simple_divider(number):
        return max(simple_dvrs)
    print('Самый большой простой делитель числа:')
    print(max_simple_divider(number))

    def max_divider(number):
        """
        :param number: integer from 1 to 10000
        :return: max divider of the number
        """
        return max(_get_dividers(number))
    print('Самый большой делитель числа:')
    print(max_divider(number))


    def get_canonical_form(number):
        Ans = []
        d = 2
        while d * d <= number:
            if number % d == 0:
                Ans.append(d)
                number //= d
            else:
                d += 1
        if number > 1:
            Ans.append(number)
        return Ans
    print('Каноническое разложение числа на простые множители')
    print(get_canonical_form(number))
else:
    print('Вы ввели число за пределами диапазона!')