import requests
import sys
import json
import time

bingMapsKey = ""

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

if not bingMapsKey or bingMapsKey == "":
    print("Token não foi inserido corretamente!")
    sys.exit()

route = "http://dev.virutalearth.net/REST/V1/Routes/Driving?wp.0=" + origin + "&wp.1=" + destination + "/&key=" + bingMapsKey
print("Printando rota... \n")
time.sleep(3)
print(route)

