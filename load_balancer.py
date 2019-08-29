# encoding: utf-8
import random

cost_total = 0
servers = []

def validation_input(ttask, task):
    """ Checks input """
    return 1


def server_calculate(input):
    return int(new_users/umax) if new_users%umax==0 else int(new_users/umax)+1


def tick():
    """ Process task for server, for user """
    global cost_total
    for i in range(len(servers)):
        servers[i] = list(map(lambda x: x-1, servers[i]))
        for element in servers[i]:
            if element == 0:
                servers[i].remove(element)
            if len(servers[i])==0:
                servers.remove(servers[i])

    cost_total += len(servers)



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


    print(new_users_)
    if new_users_>=1:
        servers.append([])
        alocate_user(new_users_)

    return servers

if __name__ == '__main__':

    ttask = int(input('Digite o número de ticks que cada tarefa leva para executar: '))
    umax = int(input('Digite quantos usuários simultâneos cada servidor suporta: '))

    servers = [[]]
    while 1:
        new_users = int(input('Digite quantos novos usuários estão conectando no sistema: '))
        servers = alocate_user(new_users)
        print(servers)
        tick()
        print(servers)
        if len(servers) == 0:
            print(cost_total)
            break;
