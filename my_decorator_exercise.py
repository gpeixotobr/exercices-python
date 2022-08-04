def my_decorator(func): # função que chama outra função que, por sua vez, tem uma função passada como parâmetro.
    def wrapper():
        print('Algo está acontecendo antes da função ser chamada')
        func()
        print('Algo está acontecendo depois da função ser chamada')
    return wrapper # retorna a própria função wrapper como retorno da função my_decorator

@my_decorator #encapsula a função que estiver imediatamente abaixo do arroba
def say_whee():
    print('whee!')

say_whee()    

@my_decorator #encapsula a função que estiver imediatamente abaixo do arroba
def say_hello():
    print('hello!')

say_hello()
