import requests
import sys
import json
import time

bingMapsKey = "Aptizt9a9YewutLyuOlZwxgKsBlE1cl4W7bqyTKpPcRfOH0BcB_zFnlEYXtlus4q"

if not bingMapsKey or bingMapsKey == "":
    print("Token não foi inserido corretamente!")
    sys.exit()

def name():
    motorista = input("Digite seu nome: ")
    return motorista

nome = name()

def quantidade_de_alunos(nome):
    numero_de_alunos = int(input(f"Certo {nome}, digite a quantidade de alunos que você tem: "))
    return numero_de_alunos

numero = quantidade_de_alunos(nome)

def ponto_inicial():
    origem = input("Digite o endereço da partida: ")
    return origem

origin = ponto_inicial()

def ponto_final():
    destinatario = input("Digite o endereço da escola: ")
    return destinatario

destinatario = ponto_final()

enderecos = []
count = 1

lista_km = []

for i in range (numero):
    endereco_aluno = input(f"Digite o endereço {count}: ")
    enderecos.append(endereco_aluno)
    count += 1

for i in enderecos:
    destination = i 

    route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + origin + "&wp.1=" + destination + "/&key=" + bingMapsKey

    print(route)

    r = requests.get(url = route)
    result = r.json()

    distance = result["resourceSets"][0]["resources"][0]["travelDistance"]

    print(distance)

    lista_km.append(distance)

lista_km.sort
print(f'A sua rota é a seguinte: {lista_km}')
lista_km.sort(reverse=True)

origin = enderecos[0]

destination = destinatario

route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + origin + "&wp.1=" + destination + "/&key=" + bingMapsKey

print(route)

r = requests.get(url = route)
result = r.json()

distance = result["resourceSets"][0]["resources"][0]["travelDistance"]

print(f"A distância do último endereço é: {distance}")
