from rest_framework import serializers

from bot_box.bot_func import send_message

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


class SlackEventSerializer(serializers.Serializer):
    type = serializers.CharField(required=False)
    user = serializers.CharField(max_length=9, required=False)
    channel = serializers.CharField(max_length=9, required=False)
    text = serializers.CharField(required=False)


class SlackDataSerializer(serializers.Serializer):
    event_time = serializers.IntegerField(required=False)
    event = SlackEventSerializer(required=False)
    challenge = serializers.CharField(required=False)
    response = serializers.CharField(required=False, read_only=True)

    class Meta:
        fields = ('event', 'challenge', 'response', 'event_time')

    def create(self, validated_data):
        if 'challenge' in validated_data:
            self.validated_data['response'] = validated_data.get('challenge')
            return self.validated_data['response']
        event_time = validated_data.get('event_time')
        print('event_time:', event_time)
        event = validated_data.get('event')
        user = event.get('user')
        channel = event.get('channel')
        type = event.get('type')
        if 'text' in event:
            text = event.get('text')
        else:
            text = ""
        response = send_message(user_input=text, user=user, channel=channel, event_time=event_time)
        self.validated_data['response'] = response
        return response

    def update(self, instance, validated_data):
        return None
