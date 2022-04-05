import datetime as dt    # Импортируйте необходимые модули

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if len(data) != 2 or data[0] is None or data[1] is None:
        return False
    else:
        return True


def check_correct_time(pack_time):
    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше самого большого ключа в словаре,
    # функция вернет False.
    # Иначе - True
    #for i in storage_data.keys():
    if storage_data and pack_time <= max(storage_data):
        return False
    else:
        return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    day_steps = sum(storage_data.values())    
    result_day = steps + day_steps
    return result_day
    

def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    transfer_coeff = 1000 # Метров в километре
    dist = steps * STEP_M / transfer_coeff
    return dist


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    # В уроке «Строки» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float
    hours = current_time.hour
    minutes = current_time.minute
    current_hours = hours + minutes/60
    mean_speed = dist / current_hours
    spent_calories = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * current_hours * 60
    return spent_calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


# Место для функции show_message.
def show_message(pack_time, day_steps, dist, spent_calories, achievement):
    print(f'\nВремя: {pack_time}.\n'
          f'Количество шагов за сегодня: {day_steps}.\n'
          f'Дистанция составила {dist:.2f} км.\n'
          f'Вы сожгли {spent_calories:.2f} ккал.\n'
          f'{achievement}\n')
    
    
def accept_package(data):
    """Обработать пакет данных."""
    # Если функция проверки пакета вернет False
    if check_correct_data(data) is False: 
        return 'Некорректный пакет'

    # Распакуйте полученные данные.
    time, steps = data
    # Преобразуйте строку с временеи в объект типа time.
    pack_time = dt.datetime.strptime(time, FORMAT).time()

    # Если функция проверки значения времени вернет False
    if check_correct_time(pack_time) is False: 
        return 'Некорректное значение времени'

    day_steps = get_step_day(steps)             # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)              # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time)  # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement) 
                                                # Вызовите функцию show_message().
    storage_data[pack_time] = steps             # Добавьте новый элемент в словарь storage_data.
    return storage_data                         # Верните словарь storage_data.


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
