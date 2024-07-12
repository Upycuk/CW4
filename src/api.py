from abc import ABC, abstractmethod

import requests
from requests import Response, JSONDecodeError

from config import HH_URL
from src.exceptions import HhAPIException


class API(ABC):
    """
    Абстрактный класс для подключения и получения данных с API ресурса.
    """

    @property
    @abstractmethod
    def url(self) -> str:
        """
        Свойства для получения url для обращения к API.
        :return:
        """
        raise NotImplementedError()


    @abstractmethod
    def get_response(self) -> Response:
        """
        Метод для подключения к API.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def get_response_data(self) -> list[dict]:
        """
        Метод для получения данных.
        :return:
        """
        raise NotImplementedError()


    @abstractmethod
    def check_status(response: Response) -> bool:
        """
        Метод для проверки статуса соединения.
        :return:
        """
        raise NotImplementedError()


class HhAPI(API):
    """
    Класс для реализации подключения и получения данных с API.
    """
    def __init__(self) -> None:
        self.__text = None
        self.__params = {
            "per_page": 100,
            "search_field": "name",
        }

    @property
    def url(self) -> str:
        """
        Получает URL.
        :return:
        """
        return HH_URL

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text

    def get_response(self) -> Response:
        """
        Получает данные.
        :return:
        """
        if self.__text is None:
            raise HhAPIException('Поисковый запрос не задан')
        self.__params["text"] = self.__text
        return requests.get(self.url, params=self.__params)

    def get_response_data(self) -> list[dict]:
        """
        Проверяет полученные данные.
        :return:
        """
        response = self.get_response()
        is_allowed = self.check_status(response)
        if not is_allowed:
            raise HhAPIException(f'Ошибка запроса данных.\nStatus Code: {response.status_code}, response: {response.text}')
        try:
            return response.json()
        except JSONDecodeError:
            raise HhAPIException(f'Ошибка получения данных.\nresponse: {response.text}')


    def check_status(response: Response) -> bool:
        """
        Проверяет статус данных.
        :param response:
        :return:
        """
        return response.status_code == 200
