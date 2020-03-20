def hello():
    print('Bom dia a todos')
    print('Esta é a quarta aula de python!')
    print('Alguém prefere JAVA?!?!?!')
    print('É claro que não')


hello()


def hello(nome):
    print('Bom dia a todos, bom dia ' + nome + '!!!!')
    print('Esta é a quarta aula de python!')
    print('Alguém prefere JAVA?!?!?!')
    print('É claro que não')


hello('Maria')


def hello(nome):
    print('Bom dia a todos, bom dia ' + nome + '!!!!')
    print('Esta é a quarta aula de python!')
    print('Alguém prefere JAVA?!?!?!')
    print('É claro que não')
    return nome

nome = hello('Manel')
print(nome)
