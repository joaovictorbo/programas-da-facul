
def cpf_validate(numbers):
    cpf = [int(char) for char in numbers]
    if len(cpf) != 11:
        return False
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True
cpf2 = ""
cpf = input("digite um cpf para ser validado")
for i in range (len(cpf)):
    if cpf[i] in "-.":
        continue
    cpf2 = cpf2+cpf[i]
validador =  cpf_validate(cpf2)

print(validador)