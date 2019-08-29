# encoding: utf-8

cost_total = 0


def validate_input(input_):
    """ Checks input """
    return input_ if input_.isdigit() and 1 <= int(input_) <= 10 else validate_input(input('Entrada inválida, digite novamente: '))


def show_servers():
    """ Show all servers with users and sum tick costs """
    global cost_total
    cost_total += len(servers)
    return ','.join(str(len(server)) for server in servers) if servers else 0


def tick(servers_):
    """ Process all process in tick time for servers """

    for i in range(len(servers_)):
        servers_[i] = list(filter(lambda process: process >= 1, list(map(lambda task: task - 1, servers_[i]))))

    return list(filter(lambda server: len(server) >= 1, servers_))


def distribute_users(new_users_, servers_, umax_, ttask_):
    """ Distribute all new users to servers """
    for server in servers_:
        if len(server) < umax_:
            if new_users_ >= umax_-len(server):
                for i in range(umax_-len(server)):
                    server.append(ttask_)
                    new_users_ -= 1

            else:
                for i in range(new_users_):
                    server.append(ttask_)
                    new_users_ -= 1

    if new_users_ >= 1:
        servers_.append([])
        distribute_users(new_users_, servers_, umax_, ttask_)

    return servers_

if __name__ == '__main__':

    ttask = int(validate_input(input('Digite o número de ticks que cada tarefa leva para executar: ')))
    umax = int(validate_input(input('Digite quantos usuários simultâneos cada servidor suporta: ')))

    servers = [[]]
    while len(servers) >= 1:
        servers = tick(servers)
        new_users = input('Digite quantos novos usuários estão conectando no sistema: ')
        servers = distribute_users(int(new_users) if new_users.isdigit() else 0, servers, umax, ttask)
        print(show_servers())
    print(cost_total)
