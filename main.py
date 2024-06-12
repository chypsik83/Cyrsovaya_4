import os
from abc import ABC

from src.HHAPI import HHAPI
from src.jsonsaver import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_vacancies_by_salary_range, \
    get_top_vacancies
from src.vacancy import Vacancy

from config import ROOT_DIR

vacancies_file_path = os.path.join(ROOT_DIR, 'data', 'vacancies.json')


def main():
    search_query = input("Введите поисковый запрос: ").split()
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HHAPI()
    json_saver_inst = JSONSaver()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filtered_vacancies = filter_vacancies(vacancies_list, search_query)
    # ranged_vacancies = get_vacancies_by_salary_range(filtered_vacancies, 20000, 3000000)
    json_saver_inst.save_filtred_vacancices(vacancies_list)  # сохраняем вакансии в формате джсон
    min_sal = input('введите минимальную зарплату : ')
    max_sal = input('введите максимальную зарплату : ')
    try:
        get_by_sal_range = get_vacancies_by_salary_range(vacancies_list, int(min_sal), int(max_sal))
    except ValueError as e:
        print(f'возникла ошибка {e}')

    sorted_vacancies = sort_vacancies(get_by_sal_range)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(filtered_vacancies) вот здесь была проблема  это печать всех вакансий
    for vacancy in top_vacancies:
        print(vacancy)
    # json_saver_inst.save_filtred_vacancices(top_vacancies)


if __name__ == "__main__":
    main()
