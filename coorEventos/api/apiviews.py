from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests
from django.contrib.auth import authenticate

from .models import Evento
from .serializers import EventoSerializer, UserSerializer

class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]


class EventoDetalle(generics.RetrieveAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]

class EventoSave(generics.CreateAPIView):
    serializer_class = EventoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Credenciales Incorrectas"},
                            status=status.HTTP_400_BAD_REQUEST)
class GetAddress(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "latlng": f"{latitude},{longitude}",
            "key": "YOURAPIKEYFROMGOOGLE",
       }
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            if data["status"] == "OK":
                formatted_address = data["results"]
                return Response({"status": "OK", "formatted_address":formatted_address})
            else:
                print("Error en la solicitud:", data["status"])
                return None
        except Exception as e:
            print("Error en la solicitud:", str(e))
            return None