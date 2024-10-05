#faça um programa que valide se um aluno pode fazer o curso de python
#onde o unico criterio é ser maior ou igual 16 anos.


idade=int(input("Qual a sua idade? "))
#recebendo informacao para validar um retorno
if(idade>=16):
    print("Sim você pode fazer o curso de Python!")
#caso nao atenda os criterios retornará
else:
    print("Não, infelizmente você nao pode fazer o curso de Python.")
    print("Curso de Python é somente para maiores de 16 anos.")