class MyClass:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                next = input(f"Для продолжения ввода нажмите пробел, для выхода из программы наберите 'stop': ")

                if next == ' ':
                    print(my_arg.my_input())
                elif next == 'stop':
                    return f'Выход'
                break


my_arg = MyClass(1)
print(my_arg.my_input())