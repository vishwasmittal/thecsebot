from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from slack_bot.serializers import SlackDataSerializer, SlackChallengeSerializer


# from .feature_selector import get_feature


class SlackResponseView(APIView):
    serializer_class = SlackDataSerializer

    def post(self, request):
        print('request.data:', request.data)
        serializer = SlackDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # text = serializer.validated_data.get('text')
        # user = serializer.validated_data.get('user')
        # channel = serializer.validated_data.get('channel')
        # feature = get_feature(text=text, user=user, channel=channel)
        response = serializer.validated_data.get('response')
        print("views, response:", response)
        return Response(response, status=status.HTTP_200_OK)


class ChallengeView(APIView):
    serializer_class = SlackChallengeSerializer

    def post(self, request):
        serializer = SlackChallengeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        return Response(serializer.data)
