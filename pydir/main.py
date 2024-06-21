#!/usr/bin/python3


"""
like-dirb tool, search for hidden pages on a web application returnin Try or False.
"""
 


# modules
from requests import get
import sys


def main(url, file):
    test  = get(url)
    if test.status_code == 200:
        print(f'\033[1;32mOK\033[m {test.status_code}')
        print(f'Search for pages on {url}')
        with open(file, 'r') as f:
            lines = f.readlines()
            for l in lines:
                new_url = f'{url}/{l}'
                r = get(new_url)
                if r.status_code == 200:
                    print(f'\033[1;32m[+]\033[m True: {new_url}')
                    with open('found_ones.txt', 'w+') as f:
                        f.write('{new_url}\n')
                else:
                    print(f'\033[1;31m[-]\033[m False: {new_url}')

    else:
        print('\033[1:31mError:\033[m {test.status_code}')
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage: ./script.py https://site.com list.txt\n")
        sys.exit(1)

    url = sys.argv[1]
    file = sys.argv[2]
    main(url, file)
