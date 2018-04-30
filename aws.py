from __future__ import print_function

import json
import urllib2
import random

print('Loading function')

def lambda_handler(event, context):
    """Main event handler from the slash command"""
    
    # dump POST to CloudWatch cuz you know this is gonna need to be dissected
    print("Received event: " + json.dumps(event, indent=2))
    resp = {
        "text":"somebody's dealing from the bottom again!",
        "attachments": [
            {
                "fallback": "new sneaky card",
                "text": "Take this card instead",
                "image_url": getCardUrl()
            }
        ]
    }
    
    # identify cheaters
    cheaterAlert()
    
    return resp

def cheaterAlert():
    """Alerts Slack users to the presence of a cheater"""
    
    cheatdata = {
        "text":"somebody's dealing from the bottom again!",
        "attachments": [
            {
                "fallback": "new sneaky card",
                "text": "Take this card instead",
                "image_url": getCardUrl()
            }
        ]
    }
    req = urllib2.Request('https://hooks.slack.com/services/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') # webhook URL to kodos channel
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(cheatdata)) # call webhook

def getCardUrl():
    """gets the image URL for a random playing card"""
    
    suits = ["H", "D", "S", "C"]
    denominations = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardUrlFormatter = "https://s3-us-west-2.amazonaws.com/plaidman1701cards/%s%s.png"

    return cardUrlFormatter % (random.choice(denominations), random.choice(suits))
