from abc import ABC, abstractmethod

import requests


class API(ABC):
    """Абстрактный класс для получения API с сайта"""

    @abstractmethod
    def get_vacancies(self, query):
        """Абстрактный метод для получения API с сайта и преобразования его в json-объекта"""
        pass
class HHAPI(API):
    """Класс для получения API с сайта по указанной вакансии """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        """
        Метод отправки запроса и получения данных из API HeadHunter
                """
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
