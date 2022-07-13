# Template para frases prontas com substituição de objetos na string.
from string import Template


templ = Template('Você está assistindo mais uma aula do curso ${curso} com o professor ${instrutor}.')
templ_2 = templ.substitute(
    curso = 'Curso de Python Avançado',
    instrutor = 'Andrézin da TI'
)

print(templ_2) 

templ_3 = Template('Também aproveite as aulas do curso de ${curso_2} com o professor ${instrutor_2}.')
dados = {
    'curso_2':'Engenharia de Dados',
    'instrutor_2':'Massao Mitsunaga'
}
templ_4 = templ_3.substitute(dados)

print(templ_4)

#fim do programa