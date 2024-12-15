# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    def __init__(self, material: str, legs_count: int):
        if legs_count <= 0:
            raise ValueError("Количество ножек стола должно быть больше нуля.")
        self.material = material
        self.legs_count = legs_count

    def assemble(self) -> str:
        """
        Собирает стол.
        :return: str
        Пример:
        >>> table = Table("дерево", 4)
        >>> table.assemble()
        'Стол из материала дерево собран.'
        """
        return f'Стол из материала {self.material} собран.'

    def clean(self) -> str:
        """
        Очищает поверхность стола.
        :return: str
        Пример:
        >>> table = Table("дерево", 4)
        >>> table.clean()
        'Стол очищен.'
        """
        return 'Стол очищен.'

    def adjust_height(self, height: float) -> str:
        """
        Регулирует высоту стола.
        :param height: float - новая высота стола
        :return: str

        Пример:
        >>> table = Table("Дерево", 4)
        >>> table.adjust_height(1.2)
        'Высота стола установлена на 1.2 м.'
        """
        return f'Высота стола установлена на {height} м.'


class Airplane:
    def __init__(self, model: str, capacity: int):
        if not model:
            raise ValueError("Модель самолета должна быть указана.")
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительным числом.")
        self.model = model
        self.capacity = capacity

    def take_off(self) -> str:
        """
        Самолет взлетает.
        :return: str
        Пример:
        >>> airplane = Airplane("Boeing 747", 300)
        >>> airplane.take_off()
        'Самолет модели Boeing 747 взлетел.'
        """
        return f'Самолет модели {self.model} взлетел.'

    def land(self) -> str:
        """
        Самолет приземляется.
        :return: str
        Пример:
        >>> airplane = Airplane("Boeing 777", 300)
        >>> airplane.land()
        'Самолет модели Boeing 777 приземлился.'
        """
        return f'Самолет модели {self.model} приземлился.'

    def board_passengers(self, passengers: int) -> str:
        """
        Посадка пассажиров на самолет.
        :param passengers: int - количество пассажиров для посадки
        :return: str
        Пример:
        >>> airplane = Airplane("Boeing 777", 300)
        >>> airplane.board_passengers(150)
        'Посажено 150 пассажиров.'
        """
        if passengers > self.capacity:
            return 'Количество пассажиров превышает вместимость!'
        return f'Посажено {passengers} пассажиров.'

class Telegram:
    def __init__(self, username: str, chat_count: int):
        if not username:
            raise ValueError("Имя пользователя не может быть пустым.")
        if chat_count < 0:
            raise ValueError("Количество чатов не может быть отрицательным.")
        self.username = username
        self.chat_count = chat_count

    def send_message(self, chat_id: int, message: str) -> str:
        """
        Отправка сообщения в чат.
        :param chat_id: int - идентификатор чата
        :param message: str - текст сообщения
        :return: str
        Пример:
        >>> telegram = Telegram("@user123", 5)
        >>> telegram.send_message(1, "Привет!")
        'Сообщение отправлено в чат 1: Привет!'
        """
        return f'Сообщение отправлено в чат {chat_id}: {message}'

    def create_chat(self, chat_name: str) -> str:
        """
        Создание нового чата.

        :param chat_name: str - название чата
        :return: str

        Пример:
        >>> telegram = Telegram("user123", 5)
        >>> telegram.create_chat("Рабочий чат")
        'Чат "Рабочий чат" создан.'
        """
        self.chat_count += 1
        return f'Чат "{chat_name}" создан.'

    def delete_chat(self, chat_id: int) -> str:
        """
        Удаление существующего чата.
        :param chat_id: int - идентификатор чата
        :return: str
        Пример:
        >>> telegram = Telegram("user123", 5)
        >>> telegram.delete_chat(1)
        'Чат 1 удален.'
        """
        if chat_id > self.chat_count:
            return 'Чат с таким идентификатором не существует.'
        self.chat_count -= 1
        return f'Чат {chat_id} удален.'
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
