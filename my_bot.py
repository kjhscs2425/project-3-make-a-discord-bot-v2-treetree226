"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
import random

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
  elif "funny" in user_message:
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
    joke= random.choice(["what did hawk one say to hawk two? tawk to the hand!", "what's white, black, and red all over? a penguin in a blender"])
    return joke #FIX HEREEEEEE
  elif "hi" in user_message:
    for i in range(5):
      return f"""hi, friend!!"""
  elif "growth mindset" in user_message:
    return user_message + " yet"
  elif "funny" in user_message:
    return "https://www.youtube.com/watch?v=LNew965FXZs"
  elif "?" in user_message:
    user_message.replace("?",)
  

  else: 
    return False
  
  

  

# def mock(user_message, user_name):
#   return 

