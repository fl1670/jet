class group_data(object):
    branch = 'yandex.ru'

    GLOBAL = {
        'Browser': {
            # 'Name': 'firefox',
            # 'Name': 'MicrosoftEdge',
            # 'Name': 'internet explorer',
            'Name': 'chrome'
        },
        'yandex.ru': {
            'Name': 'yandex.ru',
            'main_page': 'https://yandex.ru/',
            'Internal_Link': '',
            'External_Link': 'https://yandex.ru/',
            'API_Internal_Link': '',
            'API_External_Link': '',
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'Login': "",
                    'password': "",
                },
            },
            'SQL_SERVER': {
                'SERVER': '',
                'DATABASE': '',
                'user': '',
                'password': '',
                'DRIVER': '',
            }

        },
    }

    Users = {
        'User1': {
            'Login': "",
            'password': "",
            'Name': "",
        }
    }

    access_token = "",
    token_type = "",
    expires_in = ""
