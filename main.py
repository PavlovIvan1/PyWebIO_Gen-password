from pywebio import start_server, config
from pywebio.output import *
from pywebio.pin import *
import random
from string import ascii_lowercase, ascii_uppercase
from pywebio.input import input



@config(theme='sketchy')
def main():
    lower = ascii_lowercase
    upper = ascii_uppercase
    nums = '1234567890'
    symbols = '!@#$%^&*()'

    string = lower + upper + nums + symbols
    lenght = int(input("Введите длину пароля:"))
    password = "".join(random.sample(string, lenght))

    put_text(password)


if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
