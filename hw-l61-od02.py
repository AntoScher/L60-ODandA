import time


class Deque:
    def __init__(self):
        # Инициализация пустого списка для хранения элементов дека
        self.items = []

    def is_empty(self):
        # Проверка, пуст ли дек
        return len(self.items) == 0

    def size(self):
        # Возвращает количество элементов в деке
        return len(self.items)

    def add_first(self, item):
        # Добавление элемента в начало дека
        self.items.insert(0, item)

    def add_last(self, item):
        # Добавление элемента в конец дека
        self.items.append(item)

    def remove_first(self):
        # Удаление и возврат первого элемента дека
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Deque is empty"

    def remove_last(self):
        # Удаление и возврат последнего элемента дека
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Deque is empty"

    def peek_first(self):
        # Просмотр первого элемента дека без удаления
        if not self.is_empty():
            return self.items[0]
        else:
            return "Deque is empty"

    def peek_last(self):
        # Просмотр последнего элемента дека без удаления
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Deque is empty"


# Создание экземпляра дека
deque = Deque()

# Замер времени выполнения операций
start_time = time.time()

# Проверка, пуст ли дек
print("Deque is empty:", deque.is_empty())

# Добавление 10 произвольных элементов в дек (заполняется самым быстрым образом)
for i in range(10):
    deque.add_last(i)

# Печать размера дека и его элементов
print("Size of deque:", deque.size())
print("Elements in deque:", deque.items)

# Демонстрация операций с деком
print("First element (peek):", deque.peek_first())
print("Last element (peek):", deque.peek_last())
print("Removed first element:", deque.remove_first())
print("Removed last element:", deque.remove_last())
print("Elements in deque after removals:", deque.items)

# Вывод времени выполнения операций
end_time = time.time()
print("Time taken for operations:", end_time - start_time, "seconds")
