from src.utils import get_vacancies
from src.vacancy import Vacancy


def test__get_vacancies(vacancy_dict: dict, vacancy: Vacancy) -> None:
    assert get_vacancies(vacancy_dict) == [vacancy]