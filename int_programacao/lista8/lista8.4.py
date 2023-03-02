str_ = input("digite seu texto")
str_i = ""
for i in range (len(str_)):
    if str_[i] == " ":
        continue
    str_i = str_i + str_[i]
print(str_i)