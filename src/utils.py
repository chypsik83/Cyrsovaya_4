import json
import os
from config import ROOT_DIR

vacancies_file_path = os.path.join(ROOT_DIR, 'data', 'vacancies.json')


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)


def filter_vacancies(vacancies, words):
    filtered_vacancies = []
    for vacancy in vacancies:
        for word in words:
            if word in vacancy.requirement or word in vacancy.responsibility:
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def sort_vacancies(vacancies):
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies, stop):
    return vacancies[:stop]


def get_vacancies_by_salary_range(vacancies_list, salary_min: int, salary_max: int):
    """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""
    new_list = []
    for vacancy in vacancies_list:
        if isinstance(vacancy.salary, int):
            if salary_min <= vacancy.salary <= salary_max:
                new_list.append(vacancy)
    return new_list


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_path:
        return json.load(file_path)

def save_to_json(filtred_vacancies, file_path=vacancies_file_path):
    with open(file_path, 'w', encoding='utf-8') as file_path:
        json.dump(filtred_vacancies, file_path, ensure_ascii=False, indent=4)


