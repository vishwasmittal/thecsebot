from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from slack_bot.auth_classes import CSRFExemptSessionAuthentication
from slack_bot.serializers import *


# from .feature_selector import get_feature


class SlackResponseView(APIView):
    authentication_classes = (CSRFExemptSessionAuthentication, )
    serializer_class = SlackDataSerializer

    def post(self, request):
        print('\n\nrequest.data:', request.data)
        serializer = SlackDataSerializer(data=request.data)
        # if serializer.is_valid() is True:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.validated_data
        # else:
        #     serializer = SlackChallengeSerializer(data=request.data)
        #     if serializer.is_valid():
        #         response = serializer.validated_data
        #     else:
        #         return Response(data={'event': 'this field is required'}, status=status.HTTP_400_BAD_REQUEST)

        # print("response:", response)
        return Response(response, status=status.HTTP_200_OK)
