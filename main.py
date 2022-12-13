import imaplib
import email
from email.header import decode_header, make_header
from translatepy import Translator
import time
import os
from pyfiglet import Figlet

def gmail(email_adress, password):
    # Тестовая почта - u758612@gmail.com
    # Пароль приложения - lgzkhmncondmqntk
    print("="*70)
    print("Соединяюсь к почте Gmail...")
    print("="*70)
    imap_server_gmail = "imap.gmail.com"
    imap = imaplib.IMAP4_SSL(host=imap_server_gmail, port=993)
    imap.login(email_adress, password)
    imap.select("Inbox")

    _, msgnums = imap.search(None, 'ALL')

    print("="*70)
    print("Ищу файлы...")
    print("="*70)
    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum, '(RFC822)')

        massage = email.message_from_bytes(data[0][1])

        for part in massage.walk():
            if part.get_content_disposition() == "attachment":
                filename = part.get_filename()

                filename_utf8 = make_header(decode_header(filename))
                print("="*70)
                print("Скачиваю файл...")
                print("="*70)

                timestr = time.strftime("%Y%m%d_%H%M%S")
                os.mkdir(f"./load/gmail/{timestr}")

                if filename:
                    with open(f"./load/gmail/{timestr}/{filename_utf8}", 'wb') as new_file:
                        new_file.write(part.get_payload(decode=True))

                rename_file(f'./load/gmail/{timestr}/{filename_utf8}', filename_utf8, 'gmail')
    imap.close()

def mailru(email_adress, password):
    print("="*70)
    print("Пока функция для почты Mail находится на стадии разработки")
    print("="*70)

def yandexmail(email_adress, password):
    # Почта - us3r123us3r@yandex.ru
    # Пароль приложения - kjzsdkohfdrurgfh

    print("="*70)
    print("Соединяюсь к почте Yandex...")
    print("="*70)

    imap_server_yandex = "imap.yandex.ru"
    imap = imaplib.IMAP4_SSL(host=imap_server_yandex, port=993)
    imap.login(email_adress, password)
    imap.select("Inbox")

    _, msgnums = imap.search(None, 'ALL')

    print("=" * 70)
    print("Ищу файлы...")
    print("=" * 70)
    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum, '(RFC822)')

        massage = email.message_from_bytes(data[0][1])

        for part in massage.walk():
            if part.get_content_disposition() == "attachment":
                filename = part.get_filename()

                filename_utf8 = make_header(decode_header(filename))
                print("=" * 70)
                print("Скачиваю файл...")
                print("=" * 70)

                timestr = time.strftime("%Y%m%d_%H%M%S")
                os.mkdir(f"./load/yandexmail/{timestr}")

                if filename:
                    with open(f"./load/yandexmail/{timestr}/{filename_utf8}", 'wb') as new_file:
                        new_file.write(part.get_payload(decode=True))

                rename_file(f'./load/yandexmail/{timestr}/{filename_utf8}', filename_utf8, 'yandexmail')

    imap.close()

def rename_file(path_file, filename, dir_mail):
    print("="*70)
    print("Начинаю перевод имени файла")
    print("="*70)
    timestr = time.strftime("%Y%m%d_%H%M%S")
    os.mkdir(f"./translate_file/{dir_mail}/{timestr}")

    translater = Translator()

    result = translater.translate(f"{filename}", "English")

    path_file_ru = path_file

    print("="*70)
    print("Перенос файла в другую директорию")
    print("="*70)

    with open(path_file_ru, 'rb') as file:
        file_ru = file.read()

        with open(f'./translate_file/{dir_mail}/{timestr}/{result.result}', 'wb') as file_new:
            file_new.write(file_ru)

        print("="*70)
        print("Успех....")
        print("="*70)

    quit()

def main(email_type):
    if email_type.lower() == "gmail":
        print("Выбрана почта Gmail.")
        email_adress = input("Введите свою почту (пример: your-email@gmail.com): ")
        password = input("Введите пароль приложения: ")
        gmail(email_adress, password)

    elif email_type.lower() == "mail":
        print("Выбрана почта Mail")
        email_adress = input("Введите свою почту (пример: your-email@mail.ru): ")
        password = input("Введите парольот почты: ")
        mailru(email_adress, password)

    elif email_type.lower() == "yandex":
        print("Выбрана почта Yandex.")
        email_address = input("Введите свою почту (пример: your-email@yandex.ru): ")
        password = input("Введите парольот почты: ")
        yandexmail(email_address, password)

    else:
        print("="*70)
        print("Не знаю такую почту !!! ")
        print("="*70)

if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('Email Finder File'))
    print("Author: Maksim Sadkov")
    print("="*70)
    while True:
        email_type = input("\nКакой email вы используите? Введите из предложенных вариантов(Gmail, Mail, Yandex): ")
        main(email_type)