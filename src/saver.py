import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.utils import get_vacancies
from src.vacancy import Vacancy


class Saver(ABC):
    @abstractmethod
    def load_data(self):
        raise NotImplementedError()

    @abstractmethod
    def write_data(self, data) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delite_data(self, query) -> None:
        raise NotImplementedError()


class JsonSaver(Saver):
    """

    """
    def __init__(self, path: Path=Path("data")):
        self.__path = path

    def load_data(self) -> list[dict]:
        with open(self.__path, encoding='utf-8') as file:
            return json.load(file)

    def write_data(self, data: list[Vacancy]) -> None:
        old_data = self.load_data()
        old_instances = get_vacancies(old_data)

        old_id = [instance.pk for instance in old_instances]

        data_for_write = [vacancy.to_dict() for vacancy in data if vacancy.pk not in old_id]
        data_for_write.extend(old_data)
        with open(self.__path, 'w', encoding='utf-8') as file:
            json.dump(data_for_write, file, ensure_ascii=False, indent=4)

    def delite_data(self, query: dict) -> None:
        query = {
            'salary_from': 0,
            'salary_to': 1000000000,
        }

        old_data = self.load_data()
        old_instances = get_vacancies(old_data)
        filtered_instances = filter_by_salary(
            old_instances, salary_from=query['salary_from'],
            salary_to=query['salary_to']
        )
        data_for_write = [vacancy.to_dict() for vacancy in filtered_instances]
        with open(self.__path, 'w', encoding='utf-8') as file:
            json.dump(data_for_write, file, ensure_ascii=False, indent=4)
