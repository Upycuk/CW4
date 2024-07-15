class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, pk: int, name: str, salary_from: int, url: str, employer: str) -> None:
        self.__pk = pk
        self.__name = name
        self.url = url
        self.employer = employer
        self.__salary_from = self.__validate_salary(salary_from)

    @property
    def pk(self):
        return self.__pk

    @staticmethod
    def __validate_salary(salary: int) -> int:
        return 0 if salary < 0 else salary

    def __str__(self) -> str:
        return f"""
        ID: {self.__pk}
        Имя: {self.__name}
        Зарплата от {self.__salary_from}
        url: {self.url}
        Название компании: {self.employer}
    """

    def __repr__(self) -> str:
        return f"""
        ID: {self.__pk}
        Имя: {self.__name}
        Зарплата от {self.__salary_from}
        url: {self.url}
        Название компании: {self.employer}
    """

    def __lt__(self, other):
        """сортировка"""
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        """сортировка"""
        return self.__salary_from > other.__salary_from

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        return cls(
            pk=vacancy_data['pk'],
            name=vacancy_data['name'],
            url=vacancy_data['url'],
            employer=vacancy_data['employer'],
            salary_from=vacancy_data['salary_from'],
        )

    def to_dict(self) -> dict:
        return {
            'pk': self.__pk,
            'name': self.__name,
            'url': self.url,
            'employer': self.employer,
            'salary_from': self.__salary_from,
        }

    def __hash__(self):
        return hash(self.__pk)
