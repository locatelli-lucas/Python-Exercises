n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print("Com as notas {} e {}, o aluno tem uma média de {} e está \33[32mAPROVADO".format(n1, n2, media))
elif media >= 5 and media < 7:
    print("Com as notas {} e {}, o aluno tem uma média de {} e está em \33[34mRECUPERAÇÃO".format(n1, n2, media))
else:
    print("Com as notas {} e {}, o aluno tem uma média de {} e está \33[31mREPROVADO".format(n1, n2, media))