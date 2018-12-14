# coding=utf-8
# Copyright 2018 Rusty Bower
# Licensed under the Eiffel Forum License 2
import requests

from sopel.module import commands, example, NOLIMIT


def display(bot, term, data):
    definition = data['list'][0]['definition']
    bot.say('{term} - {definition})'.format(term=term, definition=definition))


def get_definition(bot, term):
    data = None
    try:
        data = requests.get('https://api.urbandictionary.com/v0/define?term={term}'.format(term=term)).json()
        return data
    except Exception:
        raise


@commands('ud', 'urban')
@example('.urban the rusty bower')
def urban(bot, trigger):
    term = trigger.group(2)
    # Get data from API
    data = get_definition(bot, term)
    # Have the bot print the data
    if data:
        if 'list' in data.keys() and len(data['list']) > 0:
            display(bot, term, data)

