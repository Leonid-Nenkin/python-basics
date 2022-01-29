
import ipaddress
import re

def get_requests(file):
    lineformat = re.compile(r"""\[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(?P<method>[a-z]{3,10}) )(?P<url>.+)(http\/1\.1"))""", re.IGNORECASE)
    res = []
    file = open(file)

    for line in file:
        ipaddress, rest_line = line.split(" - - ")
        data = re.search(lineformat, rest_line)
        res.append((ipaddress, data["method"], data["url"]))

    file.close()
    return res

if __name__=="__main__":
    file_name = "nginx_logs.txt"
    print(get_requests(file_name))