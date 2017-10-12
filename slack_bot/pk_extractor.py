import os
import json

from slack_bot.models import SlackUser as User
from bot_box.bot_func import user_info

from oauth2client import client
from apiclient import discovery
import httplib2

from slackclient import SlackClient

DEBUG = True
slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))


def LOG(message, debug=False):
    """
    To print LOG messages while execution
    :param message: The message to be printed
    :param debug: Boolean, if debug is false, no LOG messages will be printed
    :return: Nothing
    """
    file_name = globals()['__file__']
    method_name = globals()['__name__']
    if debug:
        print("LOG:", file_name, method_name + ": ", message)


def get_credentials():
    credentials = client.Credentials.new_from_json(os.environ.get("SHEET_CRED_JSON"))
    return credentials


def sheet_data():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discovery_url)
    spreadsheet_id = os.environ.get('CSE_SPREADSHEET_ID')
    data_range = 'A2:H'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=data_range).execute()
    values = result.get('values', [])  # the values stores in sheet. Each element represents a row in the sheet,
    return values


def slack_data():
    return user_info()


def pk_extractor():
    user_data = {"users": []}
    curr_user = ""
    curr_stu = 0
    count = 0
    sheet = sheet_data()
    slack = slack_data()
    for user in slack['members']:
        # print(user)
        found = False
        if user['id'] == 'USLACKBOT' or user['is_bot']:
            if DEBUG:
                print("BOT encountered")
                count += 1
            continue

        for student in sheet:
            if student[4] == user['profile']['email']:
                found = True
                curr_user = user
                curr_stu = student
                break
            elif student[1].lower().__contains__(user['profile']['first_name'].lower()) and \
                    student[1].lower().__contains__(user['profile']['last_name'].lower()):
                found = True
                curr_user = user
                curr_stu = student
                # break

        if found:
            if DEBUG:
                print("found: ", user['real_name'])
                count += 1
            # we found the and entry corresponding to the current slack user
            # now save these attributes
            curr_user_dict = {
                'name': curr_stu[1],
                'eno': curr_stu[0],
                'uid': curr_user['id'],
                'is_admin': curr_user['is_admin'],
                'user_name': curr_user['profile']['display_name'],
                'phone_no': curr_stu[2],
                'phone_no_alt': curr_stu[3],
                'dob': curr_stu[5],
                'bhawan': curr_stu[6],
                'room_no': curr_stu[7],
                'email_sheet': curr_stu[4],
                'email_slack': curr_user['profile']['email'],
            }
            user_data['users'].append(curr_user_dict)
        else:
            if DEBUG:
                print("not found: ", user['real_name'])

    if DEBUG:
        print("process complete")
        print("Count:", count)
        print("not_found:", len(slack['members']) - count)
    return user_data


def fill_user_db(user_data):
    for user in user_data['users']:
        db_user = User()
        db_user.name = user['name']
        db_user.eno = user['eno']
        db_user.uid = user['uid']
        db_user.user_name = user['user_name']
        db_user.email = user['email_slack']
        db_user.email2 = user['email_sheet']
        db_user.phone_no = user['phone_no']
        db_user.phone_no_alt = user['phone_no_alt']
        db_user.room_no = user['room_no']
        db_user.bhawan = user['bhawan']
        db_user.dob = user['dob']
        db_user.is_admin = user['is_admin']
        db_user.save()


def main():
    data = pk_extractor()
    fill_user_db(user_data=data)
    # file = open("iter1", 'w')
    # data_str = json.dumps(data, indent=4)
    # file.write(data_str)
