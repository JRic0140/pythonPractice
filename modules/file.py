import sys


def textwrited(file,datos):
    arc = open(f'./{file}','w')
    for dato in datos:

        arc.write(dato + '\n')  
    arc.close()



#            archivoPorConsola



lista = []


for con in sys.argv:
    lista.append(con)



def cont(arc = sys.argv[1],lista = sys.argv[2].split(',')):


    textwrited(arc,lista)


    print('created')
