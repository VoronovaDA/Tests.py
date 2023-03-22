def geo_logs(new_list):
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    for index in reversed(range(len(geo_logs))):
        if geo_logs[index][f'visit{index + 1}'][1] != 'Россия':
            del geo_logs[index]
    for geo in geo_logs:
        new_list.append(geo)
    return new_list


def users(ids):
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    for val in ids:
        val = list(ids.values())
        val1 = val[0]
        val2 = val[1]
        val3 = val[2]
        value = val1 + val2 + val3
        ids_new = []
        for x in value:
            if x not in ids_new:
                ids_new.append(x)
                value += ids_new
        return ids_new


def info_queries(queries):
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    dict_queries = {}

    for query in queries:
        word = len(query.split())
        if word in dict_queries.keys():
            dict_queries[word] += 1
        else:
            dict_queries.update({word: 1})

    for key, value in dict_queries.items():
        percent = round((value / len(queries)) * 100)
        return (f'Поисковых запросов из {key} слов: {value} запр. {percent}% ')
