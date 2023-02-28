valor = int(input("Qual o número da sequência que deseja saber? "))

ultimo = 1
penultimo = 1

if (valor==1) or (valor==2):
    print("1")
else:
    count=3
    while count <= valor:
        res = ultimo + penultimo
        penultimo = ultimo
        ultimo = res
        count += 1
    print(res)