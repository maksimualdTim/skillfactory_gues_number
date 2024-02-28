"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
Меньше чем за 20 попыток
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    # Воспользуемся алгоритмом бинарного поиска
    # Для этого необходимо создать отсортированный набор чисел от 1 до 100
    possible_values_list = np.arange(start=1, stop=101,step=1)
    
    low = 0
    high = len(possible_values_list) - 1

    while low <= high:
        count += 1
        mid_index = (low + high) // 2
        mid_value = possible_values_list[mid_index]
        if mid_value == number:
            break
        if mid_value > number:
            high = mid_index - 1
        else:
            low = mid_index + 1
        
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)