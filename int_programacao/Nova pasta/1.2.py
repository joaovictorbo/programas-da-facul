str_ = input("digite sua string: ")
str_i = ""
for i in range(len(str_)+1):
    str_i = str_i + str_[-i]

print(str_i)