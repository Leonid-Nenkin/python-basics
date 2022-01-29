import json

def make_dict(users_file, hobby_file):
    users = open(users_file).read().splitlines()
    hobby = open(hobby_file).read().splitlines()
    res_dict = {}

    if len(users) < len(hobby):
        exit

    for i in range(len(users)):
        d_key = ' '.join([str(elem) for elem in users[i].split(",")])
        d_value = [hobby[i]]
        res_dict[d_key] = d_value

    return res_dict

def write_to_file(res_dict):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(res_dict, f)


if __name__=="__main__":
    users_file = "users.csv"
    hobby_file = "hobby.csv"
    res = make_dict(users_file, hobby_file)
    write_to_file(res)