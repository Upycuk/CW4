class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, salary, url: str, employer: str):
        self.name = name
        self.url = url
        self.employer = employer
        self.validate_salary(salary)

    def validate_salary(self, salary):
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0

    def __str__(self):
        return f"""
        Имя: {self.name}
        Зарплата от {self.salary_from} до {self.salary_to}
        url: {self.url}
        Название компании: {self.employer}
"""

    def __lt__(self, other):
        """сортировка"""
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)