from sys import argv

salary_calc, arg_1, arg_2, arg_3 = argv

arg_1 = int(arg_1)
arg_2 = int(arg_2)
arg_3 = int(arg_3)


def salary_calc(arg_1, arg_2, arg_3):
    my_salary = (arg_1 * arg_2) + arg_3
    return my_salary


print(salary_calc)
