"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:
    def __init__(self):
        self.user_tasks = []
        self.revision_tasks = []
        self.resolved_tasks = []

    def is_empty(self):
        return self.user_tasks == []

    def to_queue(self, item):
        self.user_tasks.insert(0, item)

    def resolve_task(self, item):
        self.resolved_tasks.insert(0, item)

    def to_revision(self, item):
        self.revision_tasks.insert(0, item)

    def size(self):
        return len(self.user_tasks)

    def from_task(self):
        return self.user_tasks.pop()

    def from_revision(self):
        return self.resolved_tasks.pop()

    def show_tasks_resolved(self):
        return self.resolved_tasks


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('сделать домашнее задание')
    qc_obj.to_queue('проверить счетчики')
    qc_obj.to_queue('отправить домашку')

    print(qc_obj.is_empty())  # -> False. Очередь пустая

    print(qc_obj.size())  # -> 3
    print(qc_obj.user_tasks)
    actual_task = qc_obj.from_task()
    print(actual_task)
    command = int(input('1 - задаче решена, 2 - на доработку: '))
    if command == 1:
        qc_obj.resolve_task(actual_task)
    else:
        qc_obj.to_revision(actual_task)

    print(f'Текущие задачи: {qc_obj.user_tasks}')
    print(f'Задачи на доработке :{qc_obj.revision_tasks}')
    print(f'Решенные задачи: {qc_obj.resolved_tasks}')
