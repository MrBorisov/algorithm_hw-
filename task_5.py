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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self,el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

if __name__ == '__main__':

    sc_o = StackClass()
    print(sc_o.is_empty())
    sc_o.push_in(10)
    sc_o.push_in('code')
    sc_o.push_in(False)
    sc_o.push_in(5.5)

    print(sc_o.get_val())

def add_el(mass, el):
    index = 0
    while True:
        l = len(mass[index])
        if len(mass[index]) < 5 or len(mass[index]) == 0:
            lst = mass[index].copy()
            lst.append(el)
            mass.pop(index)
            mass.insert(index, lst)
            break
        else:
            index += 1
            if index >= 3:
                break
    return mass
elems = [[1,1,1,2,21],[1,2,2,2,2],[]]
print(add_el(elems, 1))