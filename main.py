import random
from pywebio.input import input
from pywebio.output import put_text
from pywebio import start_server

def main_func():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '1234567890'
    symbols = '!@#$%^&*()'

    string = lower + upper + nums + symbols
    lenght = int(input("Введите длину пароля:"))
    password = "".join(random.sample(string, lenght))

    put_text(password)

if __name__ == '__main__':
    start_server(main_func(), debug=False, port=5050)
