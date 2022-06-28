import requests
import sys
import json
import time

bingMapsKey = "Aptizt9a9YewutLyuOlZwxgKsBlE1cl4W7bqyTKpPcRfOH0BcB_zFnlEYXtlus4q"

if not bingMapsKey or bingMapsKey == "":
    print("Token não foi inserido corretamente!")
    sys.exit()

def name():
    nome = input("Digite seu nome: ")
    return nome

def quantidade_de_alunos():
    numero_de_alunos = int(input("Digite a quantidade de alunos que você tem: "))
    return numero_de_alunos

def ponto_inicial():
    origem = input("Digite o ponto inicial: ")
    return origem

origin = ponto_inicial()

def ponto_final():
    destinatario = input("Digite o ponto final: ")
    return destinatario

destination = ponto_final()

route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + origin + "&wp.1=" + destination + "/&key=" + bingMapsKey

print("Printando rota...\n")
print(route)

r = requests.get(url = route)
result = r.json()

distance = result["resourceSets"][0]["resources"][0]["travelDistance"]
duration = result["resourceSets"][0]["resources"][0]["travelDuration"]

print(f"\nA distância é de: {distance} km\n")

duration = duration / 60

if duration > 100:
    duration = duration / 60
    print(f"O tempo entre a partida e o destinatário é de: {duration:.0f} horas")
else:
    print(f"O tempo entre a partida e o destinatário é de: {duration:.2f} minutos")
