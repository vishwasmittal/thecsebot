from django.shortcuts import get_object_or_404

from slack_bot.models import SlackUser


def bot_info_api(query):
    user = get_object_or_404(SlackUser, uid=query.upper())
    username = user.user_name
    name = user.name
    eno = user.eno
    room_no = user.room_no
    bhawan = user.get_bhawan_display()
    phone_no = user.phone_no
    phone_no_alt = user.phone_no_alt
    email = user.email
    email2 = user.email2

    user_tuple = (username, name, eno, room_no, bhawan, phone_no, email)

    user_data = \
        """ \
Username: %s
Name: %s
E. No.: %s
Room No: %s
Bhawan: %s
Phone No: %s
Email: %s
        """ % user_tuple

    return user_data
