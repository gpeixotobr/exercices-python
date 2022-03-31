# programa que recebe login e senha do usuário, e visa impedir que o nome do usuário seja utilizado como senha

login = str(input('Nome do usuário: ')).strip
senha = str(input('Senha: ')).strip

while senha == login:
    print('ERRO! \nDigite uma senha diferente do seu nome de usuário.')
    login = str(input('Nome do usuário: ')).strip
    senha = str(input('Senha: ')).strip

# fim do programa