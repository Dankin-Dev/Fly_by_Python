if __name__ == "__main__":
    class Animal:
        """
        Базовый класс для домашних животных.
        """

        def __init__(self, name: str, age: int) -> None:
            """
            Инициализация питомца.
            :param name: Имя питомца
            :param age: Возраст питомца
            """
            self._name = name
            self.age = age

        def __str__(self) -> str:
            return f"Питомец {self._name}, возраст: {self.age}"

        def __repr__(self) -> str:
            return f"Animal(name={self._name}, age={self.age})"

        def make_sound(self) -> str:
            """
            Метод для звука питомца. Должен быть переопределен в дочерних классах.
            """
            raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

        def get_name(self) -> str:
            """
            Получение имени.
            """
            return self._name


    class Dog(Animal):
        """
        Класс, представляющий питомца собаку.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Инициализация собаки.
            :param name: Имя собаки
            :param age: Возраст собаки
            :param breed: Порода собаки
            """
            super().__init__(name, age)
            self.breed = breed

        def __str__(self) -> str:
            return f"Собака {self._name}, возраст: {self.age}, порода: {self.breed}"

        def __repr__(self) -> str:
            return f"Dog(name={self._name}, age={self.age}, breed={self.breed})"

        def make_sound(self) -> str:
            """
            Переопределение метода make_sound для собаки.
            """
            return "Гав-гав!"


    class Cat(Animal):
        """
        Класс, представляющий пиомца кошку.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            Инициализация кошки.
            :param name: Имя кошки
            :param age: Возраст кошки
            :param color: Окрас кошки
            """
            super().__init__(name, age)
            self.color = color

        def __str__(self) -> str:
            return f"Кошка {self._name}, возраст: {self.age}, окрас: {self.color}"

        def __repr__(self) -> str:
            return f"Cat(name={self._name}, age={self.age}, color={self.color})"

        def make_sound(self) -> str:
            """
            Переопределение метода make_sound для кошки.
            """
            return "Мяу-мяу!"


    dog = Dog(name="Барбос", age=3, breed="Акита-Ину")
    cat = Cat("Мурзик", 10, "Серый")
    print(dog)
    print(dog.make_sound())

    print(cat)
    print(cat.make_sound())
