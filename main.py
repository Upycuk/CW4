import logging

from src.api import HhAPI
from src.exceptions import APIException
from src.vacancy import Vacancy

logger = logging.getLogger(__name__)

def main():
    hh = HhAPI()
    hh.text = input('Введите запрос\n')
    try:
        data = hh.get_response_data()
    except APIException as a:
        logger.exception(f'Ошибка обращения к HHAPI. {a}')
        print('Что-то пошло не так :(\nПриносим наши извинения.')




if __name__ == '__main__':
    main()
