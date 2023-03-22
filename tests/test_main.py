from unittest import TestCase
from main import geo_logs, users, info_queries


class TestHomeWorks(TestCase):
    def test_visit_rus(self):
        data= [
            {'visit1': ['Москва', 'Россия']}
        ]
        geo_log = geo_logs(data)[0][f'visit{0 + 1}'][1]
        expected_geo = 'Россия'
        self.assertEqual(geo_log, expected_geo)

    def test_users_ids(self):
        data = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213, 98, 98, 35]
        }
        result_ids = users(data)
        expected_id = [213, 15, 54, 119, 98, 35]
        self.assertEqual(result_ids, expected_id)

    def test_info_queries(self):
        data = [
            'смотреть сериалы онлайн',
            'новости спорта',
            'афиша кино',
            'курс доллара',
            'сериалы этим летом',
            'курс по питону',
            'сериалы про спорт'
        ]
        for element in data:
            result = info_queries(element)
            expected = 'Поисковых запросов из 3 слов: 4 запр. 57% '
            self.assertEqual(result, expected)
