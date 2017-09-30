from rest_framework import serializers

from bot_box.feature_selector import get_feature
from bot_box.bot_func import *

''' events messages requests example

        "team_id": "T3SMAMH6W",
        "event": {
            "text": "Hi",
            "channel": "D3TJBQXSA",
            "event_ts": "1497623034.282437",
            "type": "message",
            "user": "U3SRS5L59",
            "ts": "1497623034.282437"
        },
        "token": "pa9D9E1DgHJYLT5rcOrQ3URC",
        "authed_users": [
            "U3SRS5L59"
        ],
        "event_id": "Ev5US18FL3",
        "event_time": 1497623034,
        "api_app_id": "A5UTBJ10U",
        "type": "event_callback"
    }


    personal channel
    {
        "event_id": "Ev5VDTCABE",
        "token": "pa9D9E1DgHJYLT5rcOrQ3URC",
        "event_time": 1497733590,
        "event": {
            "ts": "1497733590.778144",
            "channel": "D5VB3NJEN",
            "type": "message",
            "user": "U3SRS5L59",
            "text": "hi",
            "event_ts": "1497733590.778144"
        },
        "type": "event_callback",
        "authed_users": [
            "U3SRS5L59"
        ],
        "team_id": "T3SMAMH6W",
        "api_app_id": "A5UTBJ10U"
    }


    public channel
    {
        "event_id": "Ev5VA4RNTV",
        "token": "pa9D9E1DgHJYLT5rcOrQ3URC",
        "event_time": 1497733622,
        "event": {
            "ts": "1497733622.447095",
            "channel": "C5QLDE198",
            "type": "message",
            "user": "U3SRS5L59",
            "text": "<@U5ULW6XSL>  kaisa hai?",
            "event_ts": "1497733622.447095"
        },
        "type": "event_callback",
        "authed_users": [
            "U3SRS5L59"
        ],
        "team_id": "T3SMAMH6W",
        "api_app_id": "A5UTBJ10U"
    }
    {
        "api_app_id": "A5UTBJ10U",
        "event_time": 1497733985,
        "token": "pa9D9E1DgHJYLT5rcOrQ3URC",
        "event_id": "Ev5VA5F1PV",
        "authed_users": [
            "U3SRS5L59"
        ],
        "type": "event_callback",
        "team_id": "T3SMAMH6W",
        "event": {
            "event_ts": "1497733985.464255",
            "user": "U3SRS5L59",
            "channel": "C5QLDE198",
            "ts": "1497733985.464255",
            "text": "<#C5QLDE198|bottesting>  bottesting channel <@U3SRS5L59> cr user <@U5ULW6XSL> bakchod user <#C3SPKKJUC|general> general channel",
            "type": "message"
        }
    }

    '''


class SlackChallengeSerializer(serializers.Serializer):
    challenge = serializers.CharField()
    response = serializers.CharField(required=False)


class SlackEventSerializer(serializers.Serializer):
    type = serializers.CharField()
    user = serializers.CharField(max_length=9)
    channel = serializers.CharField(max_length=9)
    text = serializers.CharField(required=False)


class SlackDataSerializer(serializers.Serializer):
    event = SlackEventSerializer()
    response = serializers.CharField(required=False)

    class Meta:
        fields = ('event',)

    def create(self, validated_data):
        event = validated_data.get('event')
        user = event.get('user')
        channel = event.get('channel')
        type = event.get('type')
        if type == 'message':
            text = event.get('text')
        else:
            text = ""
        response = get_feature(text=text, user=user, channel=channel)
        self.validated_data['response'] = response
        send_message(channel=channel, text=response)
        return response

    def update(self, instance, validated_data):
        return None
