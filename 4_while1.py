"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    user_input = ''
    while user_input!='Хорошо':
        user_input = input('Как дела? \n').lower().capitalize()
    
if __name__ == "__main__":
    ask_user()
