import os.path
import datetime

def get_by_nickname_with_date(nickname_search, data_inicial, data_final):
    with open("logs.csv", "r") as csv_file:
        if os.path.isfile('result.txt') == True:
            os.remove('result.txt')

        init_temp = data_inicial.split('/')
        initial = datetime.datetime(int(init_temp[2]), int(init_temp[1]), int(init_temp[0]))
        final_temp = data_final.split('/')
        final = datetime.datetime(int(final_temp[2]), int(final_temp[1]), int(final_temp[0]))

        for row in csv_file:
            i = 0
            temp = row.split(',')
            nickname = temp[1]
            if nickname_search in nickname:
                with open('result.txt', 'a') as f:
                    foo = temp[3].split('/')
                    t = foo[2].split(" ")
                    bar = datetime.datetime(int(t[0]), int(foo[1]), int(foo[0]))
                    if initial <= bar <= final:
                        f.write('%-90s %-25s %-42s %2s\n' % (temp[0], temp[1], temp[2], temp[3]))


def get_by_ip_with_date(ip_search, data_inicial, data_final):
    with open("logs.csv", "r") as csv_file:

        init_temp = data_inicial.split('/')
        initial = datetime.datetime(int(init_temp[2]), int(init_temp[1]), int(init_temp[0]))
        final_temp = data_final.split('/')
        final = datetime.datetime(int(final_temp[2]), int(final_temp[1]), int(final_temp[0]))

        if os.path.isfile('result.txt') == True:
            os.remove('result.txt')
        for row in csv_file:
            i = 0
            temp = row.split(',')
            ip = temp[2]
            if ip_search in ip:
                with open('result.txt', 'a') as f:
                    foo = temp[3].split('/')
                    t = foo[2].split(" ")
                    bar = datetime.datetime(int(t[0]), int(foo[1]), int(foo[0]))
                    if initial <= bar <= final:
                        f.write('%-90s %-25s %-42s %2s\n' % (temp[0], temp[1], temp[2], temp[3]))


def get_by_path_with_date(path_search, data_inicial, data_final):
    with open("logs.csv", "r") as csv_file:

        init_temp = data_inicial.split('/')
        initial = datetime.datetime(int(init_temp[2]), int(init_temp[1]), int(init_temp[0]))
        final_temp = data_final.split('/')
        final = datetime.datetime(int(final_temp[2]), int(final_temp[1]), int(final_temp[0]))

        if os.path.isfile('result.txt') == True:
            os.remove('result.txt')
        for row in csv_file:
            i = 0
            temp = row.split(',')
            path = temp[0]
            if path_search in path:
                with open('result.txt', 'a') as f:
                    foo = temp[3].split('/')
                    t = foo[2].split(" ")
                    bar = datetime.datetime(int(t[0]), int(foo[1]), int(foo[0]))
                    if initial <= bar <= final:
                        f.write('%-90s %-25s %-42s %2s\n' % (temp[0], temp[1], temp[2], temp[3]))


def get_by_nickname(nickname_search):
    with open("logs.csv", "r") as csv_file:
        if os.path.isfile('result.txt') == True:
            os.remove('result.txt')

        for row in csv_file:
            temp = row.split(',')
            nickname = temp[1]
            if nickname_search in nickname:
                with open('result.txt', 'a') as f:
                    f.write('%-90s %-25s %-42s %2s\n' % (temp[0], temp[1], temp[2], temp[3]))


def get_by_ip(ip_search):
    with open("logs.csv", "r") as csv_file:
        if os.path.isfile('result.txt') == True:
            os.remove('result.txt')

        for row in csv_file:
            temp = row.split(',')
            ip = temp[2]
            if ip_search in ip:
                with open('result.txt', 'a') as f:
                    f.write('%-90s %-25s %-42s %2s\n' % (temp[0], temp[1], temp[2], temp[3]))


def get_by_path(path_search, data_inicial, data_final):
    with open("logs.csv", "r") as csv_file:

        if os.path.isfile('result.txt') == True:
            os.remove('result.txt')
        for row in csv_file:
            temp = row.split(',')
            path = temp[0]
            if path_search in path:
                with open('result.txt', 'a') as f:
                    f.write('%-90s %-25s %-42s %2s\n' % (temp[0], temp[1], temp[2], temp[3]))


    
# def menu():
#     opt = int(input('[1] Filtrar por nickname\n[2] Filtrar por IP\n[3] Filtrar por URL\n\nInsira a opção > '))

#     if opt == 1:
#         nickname = input('Insira o nickname desejado > ')
#         initial = input()
#         final = input()
#         get_by_nickname_with_date(nickname, initial, final)
#     elif opt == 2:
#         ip = input('Insira o IP desejado > ')
#         get_by_ip_with_date(ip)
#     elif opt == 3:
#         path = input('Insira o URL desejado > ')
#         get_by_path_with_date(path)
