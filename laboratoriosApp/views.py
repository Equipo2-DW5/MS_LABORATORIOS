from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from .models import Laboratorio
from .serializers import LaboratorioSerializer


class VerifyTokenView(TokenVerifyView):
    def post(self,request,*args,**kwargs):
        token=request.data['token']
        tokenBackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        serializer=self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            valid_data=tokenBackend.decode(token,verify=False)
            serializer.validated_data['UserId']=valid_data['user_id']
        except TokenError as e:
            raise(InvalidToken(e.args[0]))
        return Response(serializer.validated_data,status=status.HTTP_200_OK)

class RetrieveLabById(RetrieveAPIView):
    serializer_class=LaboratorioSerializer
    def get_queryset(self):
        lab_id=self.kwargs['pk']
        return Laboratorio.objects.filter(pk=lab_id)

class RetrieveLabList(ListCreateAPIView):
    serializer_class=LaboratorioSerializer
    queryset=Laboratorio.objects.all()
    def list(self,request):
        queryset = self.get_queryset()
        serializer = LaboratorioSerializer(queryset, many=True)
        return Response(serializer.data)


   # Create your views here.
