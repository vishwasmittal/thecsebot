from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from slack_bot.auth_classes import CSRFExemptSessionAuthentication
from slack_bot.serializers import *
from slack_bot.models import *
from slack_bot import pk_extractor


class SlackResponseView(APIView):
    authentication_classes = (CSRFExemptSessionAuthentication,)
    serializer_class = SlackDataSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.validated_data
        return Response(response, status=status.HTTP_200_OK)


class DatabaseUpdateView(APIView):
    # authentication_classes = (CSRFExemptSessionAuthentication)
    serializer_class = AuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        if user.is_superuser:
            pk_extractor.main()
            return Response(data={'details': 'the database is successfully updated'})
        return Response(data={'details': "user doesn't has permission to update db"}, status=status.HTTP_403_FORBIDDEN)


def sample_html(request):
    user_info = SlackUser.objects.all()
    # user_info = None
    context = {
        'users': user_info
    }
    return render(request, "users_info.html", context=context)
