def pipeline(a_list, *funcs):
    novalista = a_list
    for func in funcs:
        novalista = [(func)(i) for i in novalista ]
    return novalista

pipeline([1,2,3,4,5], lambda x: x * 2, lambda x: x-1)