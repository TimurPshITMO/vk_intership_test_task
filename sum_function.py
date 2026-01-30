# Функция для вычисления суммы чисел

def calculate_sum(numbers):
    """
    Возвращает сумму списка чисел.
    
    :param numbers: Список чисел
    :return: Сумма чисел
    """
    return sum(numbers)

# Пример использования
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = calculate_sum(nums)
    print(f"Сумма чисел {nums} = {result}")