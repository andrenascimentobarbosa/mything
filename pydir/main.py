# import request the used get function.
from requests import get

#base_url = 'https://site.com'.
base_url = ''

# path list
paths = ['robots.txt', 'login', 'wp-login.php', 'adminstrator',
        'admin', 'adm', 'assets', 'uploads', 'backup', 'analytics']
# will try one by one and make it off all the ones tha return 200 (OK) status code.
try:
    r = get(base_url)
    if r.status_code == 200:
        print('\033[1;32m[+]\033[m Connected: ', base_url)
        print()
        for w in paths:
            url = f'{base_url}/{w}'
            r = get(url)
            if r.status_code == 200:
                print(f'\033[1;32m[+]\033[m True: {url}')
            else:
                print(f'\033[1;31m[-]\033[m False: {url}')
    else:
        print(f"Couldn't connect due the error: {r.status_code}")
except Exception as e:
    print('Error: ', e)


