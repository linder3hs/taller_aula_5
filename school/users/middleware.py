from ipware import get_client_ip
from django.http import HttpResponse
import requests

"""
Vamos a crear un middleware que verifique la ip del usuario y ver
si lo dejamos pasar
"""

"""
Los middlewares recibe un parametro llamando get_response
"""

# !Vamos a crear un black list de IP que no puedo entrar a nuestro proyect
# BLACK_LIST = ['45.191.96.38']
BLACK_LIST = ['127.0.0.1']

# def is_valid_ip(get_response):
#     """
#     Esta funcion is_valid_ip va a retornar otra funcion
#     porque necesitamos comprobar que exista una respuesta al cliente
#     Puden 2 tipos de respuesta 

#     success: 201, 200
#     error: 500, 404, 403, 401
#     """
    
#     # *Esta funcion ya recibe request 

#     def middleware(request):
#         ip, is_routable = get_client_ip(request)
#         response = get_response(request)
#         print("ip", ip)
#         print("is_routable", is_routable)
#         if str(ip) in BLACK_LIST:
#             return HttpResponse("No tienes permisos", status=404)
#         else:
#             return response
    
#     return middleware


class IPIsValid:
    """
    __init__ : sirve como constructor
    __call__ : se ejecuta antes de mostrar la vista
    """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print("ip", ip)
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=40213bf4125645b6b0ef263b4aeaf88f&ip_address=" + ip)
        data = response.json()

        response = self.get_response(request)
        if data["country"] == "Peru":
            return response
        else:
            return HttpResponse("Esto es solo para Peru", status=401)
