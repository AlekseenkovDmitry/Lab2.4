class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.
    """

    def __init__(self, name: str, max_speed: float):
        """
        Инициализация транспортного средства.

        :param name: Название транспортного средства.
        :param max_speed: Максимальная скорость (в км/ч).
        """
        self.name = name
        self.max_speed = max_speed

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строка формата 'Транспортное средство: название, Максимальная скорость: ... км/ч'.
        """
        return f'Транспортное средство: {self.name}, Максимальная скорость: {self.max_speed} км/ч'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Vehicle(name=..., max_speed=...)'.
        """
        return f"Vehicle(name='{self.name}', max_speed={self.max_speed})"

    def can_overtake(self, speed_limit: float) -> bool:
        """
        Проверяет, может ли транспортное средство обогнать другой транспорт при заданном ограничении скорости.

        :param speed_limit: Ограничение скорости (в км/ч).
        :return: True, если максимальная скорость транспортного средства больше ограничения, иначе False.
        """
        return self.max_speed > speed_limit


class Car(Vehicle):
    """
    Дочерний класс, представляющий легковой автомобиль.
    Наследует базовый класс Vehicle.
    """

    def __init__(self, name: str, max_speed: float, fuel_type: str):
        """
        Инициализация легкового автомобиля.

        :param name: Название автомобиля.
        :param max_speed: Максимальная скорость (в км/ч).
        :param fuel_type: Тип топлива (например, "бензин", "дизель", "электричество").
        """
        super().__init__(name, max_speed)  # Наследуем конструктор базового класса
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строка формата 'Автомобиль: название, Максимальная скорость: ... км/ч, Тип топлива: ...'.
        """
        return f'Автомобиль: {self.name}, Максимальная скорость: {self.max_speed} км/ч, Тип топлива: {self.fuel_type}'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Car(name=..., max_speed=..., fuel_type=...)'.
        """
        return f"Car(name='{self.name}', max_speed={self.max_speed}, fuel_type='{self.fuel_type}')"

    def can_overtake(self, speed_limit: float) -> bool:
        """
        Перегрузка метода can_overtake для автомобиля.
        Автомобиль может обогнать, только если его максимальная скорость больше ограничения на 20 км/ч.

        :param speed_limit: Ограничение скорости (в км/ч).
        :return: True, если максимальная скорость автомобиля больше ограничения на 20 км/ч, иначе False.
        """
        return self.max_speed > speed_limit + 20

    def get_fuel_consumption(self, distance: float) -> float:
        """
        Возвращает примерный расход топлива на заданное расстояние.

        :param distance: Расстояние (в км).
        :return: Расход топлива (в литрах или кВт·ч).
        """
        if self.fuel_type == "бензин":
            return distance * 0.08  # Примерный расход для бензинового автомобиля
        elif self.fuel_type == "дизель":
            return distance * 0.06  # Примерный расход для дизельного автомобиля
        elif self.fuel_type == "электричество":
            return distance * 0.2  # Примерный расход для электромобиля (в кВт·ч)
        else:
            raise ValueError("Неизвестный тип топлива")


# Пример использования
if __name__ == '__main__':
    # Создаем объект базового класса
    vehicle = Vehicle(name="Грузовик", max_speed=90)
    print(vehicle)  # Проверяем __str__
    print(repr(vehicle))  # Проверяем __repr__
    print(vehicle.can_overtake(80))  # Проверяем метод can_overtake

    # Создаем объект дочернего класса
    car = Car(name="Tesla Model S", max_speed=250, fuel_type="электричество")
    print(car)  # Проверяем __str__
    print(repr(car))  # Проверяем __repr__
    print(car.can_overtake(200))  # Проверяем перегруженный метод can_overtake
    print(car.get_fuel_consumption(100))  # Проверяем метод get_fuel_consumption
