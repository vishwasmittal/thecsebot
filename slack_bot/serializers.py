from rest_framework import serializers

from .feature_selector import get_feature

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


class SlackEventSerializer(serializers.Serializer):
    text = serializers.CharField()
    user = serializers.CharField(max_length=9)
    channel = serializers.CharField(max_length=9)
    response = serializers.Field(required=False)


class SlackDataSerializer(serializers.Serializer):
    event = SlackEventSerializer()

    class Meta:
        fields = ('event',)

    def create(self, validated_data):
        text = validated_data.get('text')
        user = validated_data.get('user')
        channel = validated_data.get('channel')
        response = get_feature(text=text, user=user, channel=channel)
        return response

    def update(self, instance, validated_data):
        return "response"
