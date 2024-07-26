import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy(
        pk = 452458,
        name = 'Иван',
        salary_from = 0,
        url = 'https://api.hh.ru/vacancies',
    )


@pytest.fixture
def list_vacancy():
    return [
        Vacancy(
            pk=452458,
            name='Иван',
            salary_from=0,
            url='https://hh.ru/ivan',
        ),
        Vacancy(
            pk=5345343,
            name='Петр',
            salary_from=10,
            url='https://api.hh.ru/petr',
        )
    ]


@pytest.fixture
def vacancy_dict():
    return {
        'pk': 452458,
        'name': 'Иван',
        'salary_from': 0,
        'url': 'https://hh.ru/ivan',
    }
