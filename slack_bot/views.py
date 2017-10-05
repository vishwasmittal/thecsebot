from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from slack_bot.auth_classes import CSRFExemptSessionAuthentication
from slack_bot.serializers import *


class SlackResponseView(APIView):
    authentication_classes = (CSRFExemptSessionAuthentication,)
    serializer_class = SlackDataSerializer

    def post(self, request):
        serializer = SlackDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.validated_data
        return Response(response, status=status.HTTP_200_OK)
