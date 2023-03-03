import csv

with open("data.csv","r") as file:
        data = csv.reader(file, delimiter="\t")

def pregunta_01():
    x = 0
    for row in data:
        x += int(row[1])
    return x

if __name__ == '__main__':
    x = pregunta_01()
    print(x)

#print(pregunta_01())

# from csv import reader

# def pregunta_02():

    
#     with open("data.csv","r") as csvfile:
#         data = reader(csvfile, delimiter="\t")
#         letras = []
#         letras_org = {}
#         for row in data:
#             letras += row[0]
#         letras_org = sorted(set(letras))
#         #print((letras))
#         #print((letras_org))
#         lista = []
#         for cuenta in letras_org:
#             tupla_a = (cuenta,letras.count(cuenta))
#             lista.append(tupla_a)
#         print(lista)

#     return

# print(pregunta_02())