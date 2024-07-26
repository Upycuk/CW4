import logging

from src.api import HhAPI
from src.exceptions import APIException
from src.saver import JsonSaver
from src.utils import get_vacancies
from src.vacancy import Vacancy

logger = logging.getLogger(__name__)

def main():
    user_name = input("Как ваше имя?\n")
    user_input = input(f'''Добро пожаловать, {user_name}, выберите действия: 
        1. загрузить доступные вакансии по ключевому слову.
        2. вывести топ вакансий.\n''')

    if not user_input.isdigit():
        pass

    user_answer = int(user_input)

    hh = HhAPI()
    hh.text = input('Введите ваш запрос\n')
    try:
        data = hh.get_response_data()
    except APIException as f:
        logger.exception(f'Ошибка обращения к API. {f}')
        print('Что-то пошло не так :(\nПриносим наши извинения.')

    if user_answer == 1:
        vacancies = get_vacancies(data)
        print('Сохраняем вакансии в файл...\n')
        saver = JsonSaver()
        saver.write_data(vacancies)

    elif user_answer == 2:
        vacancies = get_vacancies(data)
        for vac in sorted(vacancies, reverse=True)[:5]:
            print(vac)


if __name__ == '__main__':
    main()
