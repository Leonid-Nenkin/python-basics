import re

def email_parse(email_address):
    regex = re.compile(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')
    assert regex.match(email_address)

    keys = ['username', 'domain']
    res = dict(zip(keys, regex.findall(email_address)[0].split('@')))
    return res

if __name__ == "__main__":
    print(email_parse('name@domain.ru'))

