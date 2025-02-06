"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
import random
from emoji import EMOJI_DATA
from string import punctuation
from collections import Counter

emojis = list(EMOJI_DATA.keys())

def vowelOrConsonant(x): 
    if (x == 'a' or x == 'e' or x == 'i' or 
        x == 'o' or x == 'u' or x == 'A' or 
        x == 'E' or x == 'I' or x == 'O' or 
        x == 'U'): 
        return random.choice(emojis)
    else: 
        return random.choice(punctuation)

def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  elif "mock" in user_message:
    return True
  elif "joke" in user_message:
    return True
  elif "hi" in user_message:
    return True
  elif "growth mindset" in user_message:
    return True
  elif "?" in user_message:
    return True
  elif "funny" in user_message:
    return True
  elif "beer" in user_message:
    return True
  elif "grentperez" in user_message:
    return True
  elif "random" in user_message:
    return True
  elif "counter" in user_message:
    return True
  else: 
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if "robot" in user_message:
    return f"""you said my name!!
  {user_message.replace("robot", user_name)}"""
  elif "mock" in user_message:
    word = ""
    for thingy, letter in enumerate(user_message):
      word += letter.upper() if thingy % 2 else letter
    return word
  elif "joke" in user_message:
    joke= random.choice(["what did hawk one say to hawk two? tawk to the hand!", "what's white, black, and red all over? a penguin in a blender", "What did the fish say when he swam into a wall? Dam.", "What do you call a fish with no eyes? Fsh.", "What do you call a can opener that doesn’t work? A can’t opener! "])
    return joke 
  elif "hi" in user_message:
    nickname= user_name[0:3]
    return f"""hi, {nickname}!!"""
  elif "growth mindset" in user_message:
    return user_message + " yet"
  elif "funny" in user_message:
    return "https://www.youtube.com/watch?v=LNew965FXZs"
  elif "?" in user_message:
    return f"""You say: {user_message}"
    {user_message.replace("?", "!")}"""
  elif "beer" in user_message:
    return f"""beerrrrrrrrrr!!"""
  elif "grentperez" in user_message:
    return f"""https://www.grentperez.com/"""
  elif "random" in user_message:
    x = ""
    for letter in user_message:
      x+= vowelOrConsonant(letter)
    return x
  elif "counter" in user_message:
    counter = Counter(user_message)
    ah= counter['z']
    return f"""there are {ah} z's in your message"""
  else: 
    return False