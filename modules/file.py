
def textwrited(file,datos):
    arc = open(f'./result/{file}','w')
    for dato in datos:

        arc.write(dato + '\n')  

    print('textWrited error 0')

    arc.close()