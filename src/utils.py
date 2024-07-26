from src.vacancy import Vacancy


def get_vacancies(vacancies: list[dict]) -> list[Vacancy]:
    # print(f'DEBUG {vacancies}')
    return [Vacancy.create_vacancy(vacancy) for vacancy in vacancies]


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(vacancies, reverse=True)
