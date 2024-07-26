class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, pk: int, name: str, salary_from: int, salary_to: int, url: str) -> None:
        self.__pk = pk
        self.__name = name
        self.url = url
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)

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
    """

    def __repr__(self) -> str:
        return f"""
        ID: {self.__pk}
        Имя: {self.__name}
        Зарплата от {self.__salary_from}
        url: {self.url}        
    """

    def __lt__(self, other):
        """сортировка"""
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        """сортировка"""
        return self.__salary_from > other.__salary_from

    @staticmethod
    def valid_vacancy_data(vacancy_data):
        if not vacancy_data.get('salary_from'):
            vacancy_data['salary_from'] = 0
        if not vacancy_data.get('salary_to'):
            vacancy_data['salary_to'] = 0
        return vacancy_data

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        vacancy_data = cls.valid_vacancy_data(vacancy_data)
        return cls(
            pk=vacancy_data['id'],
            name=vacancy_data['name'],
            salary_from=vacancy_data['salary_from'],
            salary_to=vacancy_data['salary_to'],
            url=vacancy_data['url'],
        )

    def to_dict(self) -> dict:
        return {
            'id': self.__pk,
            'name': self.__name,
            'salary_from': self.__salary_from,
            'salary_to': self.__salary_to,
            'url': self.url,
        }

    def __hash__(self):
        return hash(self.__pk)
