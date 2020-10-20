from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
import pickle
import numpy as np

@api_view(['POST'])
def Robo(request):

                valor_K = float(request.POST['K'])
                valor_NA = int(request.POST['NA'])
                valor_UREIA = int(request.POST['UREIA'])
                valor_CREAT = float(request.POST['CREAT'])

                naive_bayes = pickle.load(open('core/ArquivoRobo/robo.sav', 'rb'))
                novo_registro = [[valor_K,valor_NA,valor_UREIA,valor_CREAT]]
                novo_registro = np.asarray(novo_registro)
                resposta = naive_bayes.predict_proba(novo_registro)

                return HttpResponse(resposta)
        
       