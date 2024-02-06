from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from PIL import Image
from io import BytesIO
from django.contrib.messages import constants
from django.contrib import messages

# A função (obter_imagem_do_pokemon) desenvolvida para poder fazer o retorno da imagem que
# esta contida na url, para poder realizar essa manipulação foi
# necessario instalar o pillow

def obter_imagem_do_pokemon(url):
    response = requests.get(url)
    imagem_bytes = BytesIO(response.content)
    imagem = Image.open(imagem_bytes)
    return imagem

# A função (habilidades) ela executa uma interação sobre uma lista
# assim conseguindo filtrar as informações necessarias para enviar para
# o template

def habidades(poke):
   for i in poke['abilities']:
      print(i['ability']['name'])

# a função (inicio) ela inicia recebendo uma requisição tipo POST
# após isso passo a url da api de onde os dados serão extraidos
# depois o response faz um requisição tipo GET para a url fornecida
# construida com a biblioteca requests que foi instalada no inicio do projeto
# OBS: passei três variaveis vazias que serão adicionadas valores durante a requisição
      
    
def inicio(request):
    poke = None
    url_imagem_pokemon = None
    habilidades_pokemon = None
    
    if request.method == "POST":
        pokemon = request.POST.get('pokemon')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
        response = requests.get(url)
        
        if response.status_code == 200:
            poke = response.json()
            habidades
            url_imagem_pokemon = poke.get("sprites", {}).get("front_default", "")

        if url_imagem_pokemon:  
            imagem_pokemon = obter_imagem_do_pokemon(url_imagem_pokemon)
            poke["imagem_pokemon"] = imagem_pokemon
            habilidades_pokemon = [i['ability']['name'] for i in poke.get('abilities', [])]

        if poke and 'name' in poke and poke['name']:
            pass
        else:
             messages.add_message(request, constants.ERROR, 'O Pokémon não foi encontrado em nosso banco de dados')
             redirect('inicio')
            
    context = {'poke': poke, 'habilidades_pokemon': habilidades_pokemon}
    return render(request, 'index2.html', context)
   
        

      
    
    

   