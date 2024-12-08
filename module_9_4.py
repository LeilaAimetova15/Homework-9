first = 'Мама мыла раму'
second = 'Рамена мало было'
#Lambda-функция:
print(list(map(lambda x, y: x == y, first, second)))
#Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#Метод __call__:
import random
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно')
print(first_ball())
print(first_ball())
print(first_ball())