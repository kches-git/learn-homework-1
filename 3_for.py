"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_of_all_scores = [{"school_class": "1a", "scores": [5,4,4,5,4]}, {"school_class": "2a", "scores": [5,4,4,5,5]}, {"school_class": "3a", "scores": [3,4,4,5,2]}, {"school_class": "5a", "scores": [3,4,4,3,5]}]
    school_scores = [] 

    for c in list_of_all_scores:
        school_scores += c["scores"]

    school_avg_score = sum(school_scores) / len(school_scores)
    print(f"Средний балл по школе – {school_avg_score}")

    for c in list_of_all_scores:
        class_avg_score = sum(c["scores"]) / len(c["scores"])
        class_name = c["school_class"]
        print(f"Cредний балл по классу {class_name} – {class_avg_score}")

if __name__ == "__main__":
    main()
