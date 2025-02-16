if __name__ == "__main__":
    class Planes:
        """
        Базовый класс для представления самолетов.

        Атрибуты:
            _model (str): Модель самолета.
            _wingarea (float): Площадь крыла (в квадратных метрах).
            _thrust (float): Тяга двигателя (в Ньютонах).
            _price (int): Стоимость самолета (в USD).
            _weight (float): Вес самолета (в Ньютонах).
        """

        def __init__(self):
            """Инициализирует атрибуты самолета."""
            self._model = None
            self._wingarea = None
            self._thrust = None
            self._price = None
            self._weight = None

        @property
        def wingarea(self) -> float:
            """
            Возвращает площадь крыла самолета.

            :return: Площадь крыла (в квадратных метрах).
            """
            return self._wingarea

        @wingarea.setter
        def wingarea(self, len: float):
            """
            Устанавливает площадь крыла самолета.

            :param len: Площадь крыла (в квадратных метрах).
            :raises ValueError: Если площадь крыла отрицательная или не является типом float.
            """
            if not isinstance(len, float):
                print('Площадь крыла должен быть типа float')
            if len < 0:
                print('Площадь крыла должен быть положительным числом')
            self._wingarea = len

        @property
        def thrust(self) -> float:
            """
            Возвращает тягу двигателя самолета.

            :return: Тяга двигателя (в Ньютонах).
            """
            return self._thrust

        @thrust.setter
        def thrust(self, value: float):
            """
            Устанавливает тягу двигателя самолета.

            :param value: Тяга двигателя (в Ньютонах).
            :raises ValueError: Если тяга отрицательная или не является типом float.
            """
            if not isinstance(value, float):
                print('Тяга должен быть типа float')
            if value < 0:
                print('Тяга должена быть положительным числом')
            self._thrust = value

        @property
        def price(self) -> int:
            """
            Возвращает стоимость самолета.

            :return: Стоимость самолета (в USD).
            """
            return self._price

        @price.setter
        def price(self, value: int):
            """
            Устанавливает стоимость самолета.

            :param value: Стоимость самолета (в USD).
            :raises ValueError: Если стоимость отрицательная или не является типом int.
            """
            if not isinstance(value, int):
                print('Стоимость быть типа int')
            if value < 0:
                print('Стоимость должена быть положительным числом')
            self._price = value

        @property
        def model(self) -> str:
            """
            Возвращает модель самолета.

            :return: Модель самолета.
            """
            return self._model

        @model.setter
        def model(self, simbols: str):
            """
            Устанавливает модель самолета.

            :param simbols: Модель самолета.
            :raises ValueError: Если модель не является типом str.
            """
            if not isinstance(simbols, str):
                print('Имя должно быть типа str')
            self._model = simbols

        @property
        def weight(self) -> float:
            """
            Возвращает вес самолета.

            :return: Вес самолета (в Ньютонах).
            """
            return self._weight

        @weight.setter
        def weight(self, value: float):
            """
            Устанавливает вес самолета.

            :param value: Вес самолета (в Ньютонах).
            :raises ValueError: Если вес отрицательный или не является типом float.
            """
            if not isinstance(value, float):
                print('Вес должен быть типа float')
            if value < 0:
                print('Вес должен быть положительным числом')
            self._weight = value

        def calculate_thrust_to_weight_ratio(self) -> float:
            """
            Рассчитывает тяговооружённость (отношение тяги к весу).

            :return: Тяговооружённость.
            :raises ValueError: Если вес самолета не задан или равен нулю.
            """
            if self._weight is None or self._weight == 0:
                raise ValueError("Вес самолета не задан или равен нулю.")
            return self._thrust / self._weight

        def calculate_wing_loading(self) -> float:
            """
            Рассчитывает удельную нагрузку на крыло (отношение веса к площади крыла).

            :return: Удельная нагрузка на крыло.
            :raises ValueError: Если площадь крыла не задана или равна нулю.
            """
            if self._wingarea is None or self._wingarea == 0:
                raise ValueError("Площадь крыла не задана или равна нулю.")
            return self._weight / self._wingarea

        def __repr__(self):
            """
            Возвращает строковое представление объекта для разработчика.

            :return: Строка, содержащая информацию о самолете.
            """
            return f'{self.__class__.__name__}(model={self._model!r}, wingarea={self._wingarea!r}, ' \
                   f'thrust={self._thrust!r}, price={self._price!r}, weight={self._weight!r})'

        def __str__(self):
            """
            Возвращает строковое представление объекта для пользователя.

            :return: Строка, содержащая модель и цену самолета.
            """
            return f"Модель самолёта: '{self._model}', Цена: '{self._price}', Вес: '{self._weight}'"

    class PassengerPlane(Planes):
        """
        Дочерний класс для представления пассажирских самолетов.

        Атрибуты:
            _passenger_capacity (int): Вместимость пассажиров.
        """

        def __init__(self):
            """Инициализирует атрибуты пассажирского самолета."""
            super().__init__()
            self._passenger_capacity = None

        @property
        def passenger_capacity(self) -> int:
            """
            Возвращает вместимость пассажиров.

            :return: Вместимость пассажиров.
            """
            return self._passenger_capacity

        @passenger_capacity.setter
        def passenger_capacity(self, value: int):
            """
            Устанавливает вместимость пассажиров.

            :param value: Вместимость пассажиров.
            :raises ValueError: Если вместимость отрицательная или не является типом int.
            """
            if not isinstance(value, int):
                print('Вместимость пассажиров должна быть типа int')
            if value < 0:
                print('Вместимость пассажиров должна быть положительным числом')
            self._passenger_capacity = value

        def __repr__(self):
            """
            Возвращает строковое представление объекта для разработчика.

            :return: Строка, содержащая информацию о пассажирском самолете.
            """
            return f'{self.__class__.__name__}(model={self._model!r}, wingarea={self._wingarea!r}, ' \
                   f'thrust={self._thrust!r}, price={self._price!r}, weight={self._weight!r}, ' \
                   f'passenger_capacity={self._passenger_capacity!r})'

        def __str__(self):
            """
            Возвращает строковое представление объекта для пользователя.

            :return: Строка, содержащая модель, вместимость и цену пассажирского самолета.
            """
            return f"Пассажирский самолёт: '{self._model}', Вместимость: '{self._passenger_capacity}', Цена: '{self._price}'"

    class CargoPlane(Planes):
        """
        Дочерний класс для представления грузовых самолетов.

        Атрибуты:
            _cargo_capacity (float): Грузоподъемность (в Ньютонах).
        """

        def __init__(self):
            """Инициализирует атрибуты грузового самолета."""
            super().__init__()
            self._cargo_capacity = None

        @property
        def cargo_capacity(self) -> float:
            """
            Возвращает грузоподъемность самолета.

            :return: Грузоподъемность (в Ньютонах).
            """
            return self._cargo_capacity

        @cargo_capacity.setter
        def cargo_capacity(self, value: float):
            """
            Устанавливает грузоподъемность самолета.

            :param value: Грузоподъемность (в Ньютонах).
            :raises ValueError: Если грузоподъемность отрицательная или не является типом float.
            """
            if not isinstance(value, float):
                print('Грузоподъемность должна быть типа float')
            if value < 0:
                print('Грузоподъемность должна быть положительным числом')
            self._cargo_capacity = value

        def calculate_wing_loading(self) -> float:
            """
            Перегруженный метод для расчета удельной нагрузки на крыло.
            У грузовых самолетов нагрузка на крыло обычно выше из-за груза.

            :return: Удельная нагрузка на крыло.
            :raises ValueError: Если площадь крыла не задана или равна нулю.
            """
            if self._wingarea is None or self._wingarea == 0:
                raise ValueError("Площадь крыла не задана или равна нулю.")
            return (self._weight + self._cargo_capacity) / self._wingarea

        def __repr__(self):
            """
            Возвращает строковое представление объекта для разработчика.

            :return: Строка, содержащая информацию о грузовом самолете.
            """
            return f'{self.__class__.__name__}(model={self._model!r}, wingarea={self._wingarea!r}, ' \
                   f'thrust={self._thrust!r}, price={self._price!r}, weight={self._weight!r}, ' \
                   f'cargo_capacity={self._cargo_capacity!r})'

        def __str__(self):
            """
            Возвращает строковое представление объекта для пользователя.

            :return: Строка, содержащая модель, грузоподъемность и цену грузового самолета.
            """
            return f"Грузовой самолёт: '{self._model}', Грузоподъемность: '{self._cargo_capacity}', Цена: '{self._price}'"

    # Пример использования
    passenger_plane = PassengerPlane()
    passenger_plane.model = "Boeing 747"
    passenger_plane.wingarea = 511.0
    passenger_plane.thrust = 1200000.0
    passenger_plane.price = 250000000
    passenger_plane.weight = 183500.0
    passenger_plane.passenger_capacity = 416

    print(passenger_plane)
    print(repr(passenger_plane))
    print("Тяговооружённость:", passenger_plane.calculate_thrust_to_weight_ratio())
    print("Удельная нагрузка на крыло:", passenger_plane.calculate_wing_loading())

    cargo_plane = CargoPlane()
    cargo_plane.model = "Antonov An-225"
    cargo_plane.wingarea = 905.0
    cargo_plane.thrust = 1400000.0
    cargo_plane.price = 300000000
    cargo_plane.weight = 285000.0
    cargo_plane.cargo_capacity = 250000.0

    print(cargo_plane)
    print(repr(cargo_plane))
    print("Тяговооружённость:", cargo_plane.calculate_thrust_to_weight_ratio())
    print("Удельная нагрузка на крыло (с учетом груза):", cargo_plane.calculate_wing_loading())