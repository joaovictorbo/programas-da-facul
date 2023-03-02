data = input("digite sua data de aniversario assim(01/01/2000)")
mes = data[3:5]
dia = data[:3]
ano = data[5:]
if mes == "01":
    mes = "janeiro"
if mes == "02":
    mes = "fevereiro"
if mes == "03":
    mes = "março"
if mes == "04":
    mes = "maio"
if mes == "05":
    mes = "abril"
if mes == "06":
    mes = "junho"
if mes == "07":
    mes = "julho"
if mes == "08":
    mes = "agosto"
if mes == "09":
    mes = "setembro"
if mes == "10":
    mes = "outubro"
if mes == "11":
    mes = "novembro"
if mes == "12":
    mes = "dezembro"

print(dia+mes+ano)

