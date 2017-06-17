"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import json
import speech_recognition as sr
from voice import record_to_file
from os import path


def recognize_speech(audio_file):
    "Edu papa bless boiii you da best"
    r = sr.Recognizer()
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio_file)
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
    return text


lex_session = Session(profile_name="adminuser", region_name="us-east-1")
lex = lex_session.client("lex-runtime")

def stop():
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='Stop'
    )

def getMessage(response):
    if(response['dialogState'] == 'ConfirmIntent'):
        return response['message']
    elif(response['dialogState'] == 'ReadyForFulfillment'):
        return "ReadyForFulfillment"
    elif(response['dialogState'] == 'Failed'):
        return response['message']
    else:
        return None


def call_police():

    text = recognize_speech(record_to_file('test1.wav'))
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText=text
    )
    return getMessage(response)


def eyes_closed():
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='TRIGGER COPILOT'
    )
    return getMessage(response)


def find_nearest_gas_station():
    pass


def play_music():
    pass


def stop():
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='Stop'
    )


def text_contact(person):
    from contact_list import contact_list
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='text %s' % person
    )
    contact = response['slots']['CONTACT']
    if contact in contact_list:
        print(contact_list[contact])
    # return response


def yes():
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='Yes'
    )
    return getMessage(response)


def no():
    response = lex.post_text(
     botName='CopilotBot',
     botAlias='Prod',
     userId='TheRubberDucks',
     sessionAttributes={
         'string': 'string'
     },
     inputText='No'
    )
    return getMessage(response)

def spoken_no():
    response = lex.post_content(
        botName='CopilotBot',
        botAlias='Prod',
        userId='pablopg',
        sessionAttributes={
            'string': 'string'
        },
        accept = 'text/plain; charset=utf-8',
        contentType='audio/',
        inputStream= 'https://s3.eu-west-2.amazonaws.com/static-server-for-rendering-xml/no.opus'
    )

    print(response)
    return getMessage(response)