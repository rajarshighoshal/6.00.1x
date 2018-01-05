# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:28:45 2017

@author: RAJARSHI GHOSHAL
"""

from ps6 import *

def decrypt_story():
    story = get_story_string()
    encrypted_story = CiphertextMessage(story)
    decrypted_story = encrypted_story.decrypt_message()
    return decrypted_story
