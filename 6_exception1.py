"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    dict = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как погода?": "Солнечно!", "Когда отдыхать?": "Покой нам только снится =)"}
    
    while True:    
        try:
            user_input = input('\nВведите ваш вопрос: \n').lower().capitalize()
            print(dict.get(user_input, "Я вас не понимаю"))
        except KeyboardInterrupt:
            print('Пока!')
            break    

if __name__ == "__main__":
    ask_user()
