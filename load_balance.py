# encoding: utf-8
import random

cost_total = 0
servers = []

def validation_input(ttask, task):
    """ Checks input """
    return 1


def show_servers():
    global cost_total
    cost_total += len(servers)
    return ','.join(str(len(server)) for server in servers)


def tick():
    """ Process task for server, for user """
    global servers

    for i in range(len(servers)):
        servers[i] = list(filter(lambda a: a>=1,list(map(lambda x: x-1, servers[i]))))

    servers = list(filter(lambda lenght: len(lenght)>=1,servers))





def alocate_user(new_users_):
    for server in servers:
        if len(server)<umax:
            if new_users_ >= umax-len(server):
                for i in range(umax-len(server)):
                    server.append(ttask)
                    new_users_ -= 1

            else:
                for i in range(new_users_):
                    server.append(ttask)
                    new_users_ -= 1



    if new_users_>=1:
        servers.append([])
        alocate_user(new_users_)

    return servers

if __name__ == '__main__':

    ttask = int(input('Digite o número de ticks que cada tarefa leva para executar: '))
    umax = int(input('Digite quantos usuários simultâneos cada servidor suporta: '))

    servers = [[]]
    while len(servers) >= 1:
        tick()
        new_users = int(input('Digite quantos novos usuários estão conectando no sistema: '))
        servers = alocate_user(new_users)
        print(show_servers())
    print(cost_total)
