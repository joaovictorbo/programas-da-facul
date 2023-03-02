# -*- coding: utf-8 -*-
msg = "teste"
def cript(msg, chave = 10):
    str_retorno =  ""
    max = 126
    for a in msg:
        num_cript = ord(a) + chave
    
        if(num_cript > max):
            num_cript = 31 + (num_cript % max)
        
        char_crip = chr(num_cript)
    
        str_retorno = str_retorno + char_crip
        
    return str_retorno

def uncript(msg, chave = 10):
    str_retorno =  ""
    min = 32
    for a in msg:
        num_cript = ord(a) - chave
    
        if(num_cript < min):
            num_cript = 31 + (num_cript % min)
        
        char_crip = chr(num_cript)
    
        str_retorno = str_retorno + char_crip
        
    return str_retorno
cript(msg)

uncript(msg)
    

# filename = "test.txt"
# filename_out = "out.txt"

# file_out = open(filename_out, 'w+')

# with open(filename, 'r', errors='ignore') as file:
#     for line in file:
#         print(line)
#         cript_line = cript(line[:len(line)-1], chave)
#         #print(cript_line)
#         file_out.write(cript_line + "\n")
        
# file_out.close()