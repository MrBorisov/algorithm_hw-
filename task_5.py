"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:
    def __init__(self):
        self.elems = [[], [], []]

    def is_empty(self):
        return self.elems == [[], [], []]

    def push_in(self, el):
        index = 0
        while True:
            if len(self.elems[index]) < 5 or len(self.elems[index]) == 0:
                lst = self.elems[index].copy()
                lst.append(el)
                self.elems.pop(index)
                self.elems.insert(index, lst)
                break
            else:
                index += 1
                if index >= 3:
                    break
        return self.elems

    def pop_out(self):
        index = len(self.elems) - 1
        while index >= 0:
            if self.elems[index] == []:
                index -= 1
            else:
                lst = self.elems[index].copy()
                lst.pop()
                self.elems.pop(index)
                self.elems.insert(index, lst)
                break

    def get_val(self):
        index = len(self.elems) - 1
        while True:
            if self.elems[index] == []:
                index -= 1
            else:
                return self.elems[index][-1]

    def stack_size(self):
        index = len(self.elems) - 1
        while True:
            if self.elems[index] == []:
                index -= 1
            else:
                return len(self.elems[index])


if __name__ == '__main__':

    sc_o = StackClass()
    print(sc_o.is_empty())
    sc_o.push_in(10)
    sc_o.push_in('code')
    sc_o.push_in(False)
    sc_o.push_in(5.5)
    sc_o.push_in(55.5)
    sc_o.pop_out()
    print(sc_o.get_val())
    print(sc_o.elems)
    print(sc_o.stack_size())
