# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    def __init__(self, material: str, height: float, length: float):
        if not isinstance(material, str):
            raise TypeError
        if not isinstance(height, float):
            raise TypeError
        if not isinstance(length, float):
            raise TypeError
        if (height < 0) or (length < 0):
            raise ValueError

        self.material = material
        self.height = height
        self.length = length

        def compute_area(self, height: float, length: float):
            if not isinstance(height, float):
                raise TypeError
            if not isinstance(length, float):
                raise TypeError
            if (height < 0) or (length < 0):
                raise ValueError

            area = height * length

            return area

        def sanitize_top(self) -> None:
            '''
            Очищает поверхность стола.

            #return: None

            #table = Table("металл", 70, 140)
            # table.sanitize_top()'''

class Tree:
    def __init__(self, species: str, height: float, age: int):
        if not isinstance(species, str):
            raise TypeError
        if not isinstance(height, float):
            raise TypeError
        if not isinstance(age, float):
            raise TypeError
        if (height < 0) or (age < 0):
            raise ValueError

        def increase_height(self, years: int) -> None:

            """
            Увеличивает возраст и высоту дерева.

            :param years: Количество лет роста.
            :raises ValueError: Если years меньше или равно 0.
            :return: None

            tree = Tree("дуб", 5, 10)
            tree.increase_height(5)
            """

        def generate_oxygen(self) -> float:
            """
            Вычисляет количество кислорода, которое производит дерево за год.

            :return: Количество кислорода в килограммах.

            tree = Tree("сосна", 10, 15)
            tree.generate_oxygen()
            """
class Facebook:
    def __init__(self, users: int, daily_posts: int):
        if not isinstance(users, int):
            raise TypeError
        if not isinstance(daily_posts, int):
            raise TypeError
        if users < 0 or daily_posts < 0:
            raise ValueError("Количество пользователей и публикаций не может быть отрицательным.")
        self.users = users
        self.daily_posts = daily_posts

    def register_user(self, count: int) -> None:
        """
        Добавляет пользователей.

        :param count: Количество добавленных пользователей.
        :raises ValueError: Если count меньше 0.
        :return: None

        fb = Facebook(1000, 500)
        fb.register_user(100)
        """
        ...

    def compute_engagement(self) -> float:
        """
        Вычисляет коэффициент вовлеченности на основе публикаций и пользователей.

        :return: Коэффициент вовлеченности (0 <= rate <= 1).

        fb = Facebook(1000, 500)
        fb.compute_engagement()
        """
        ...
