import hashlib

import requests
import hashlib


def guest_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching', {res.status_code}, 'change again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)


def pwed_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-32')).hexdigest().upper()
    first_5char, tail = sha1_password[:5], sha1_password[5:]
    response = guest_api_data(first_5char)
    # print(response)
    return get_password_leaks_count(response, tail)

pwed_api_check('123')
