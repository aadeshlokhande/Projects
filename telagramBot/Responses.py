import calendar
from datetime import datetime
import os 

# os.system("pip install python-telegram-bot")
try:
    import cryptocompare
except:
    os.system("pip install cryptocompare")
    import cryptocompare

try:
    import emojis
except:
    os.system("pip install emojis")
    import emojis

try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet

try:
    import pyshorteners
except:
    os.system("pip install pyshorteners")
    import pyshorteners

try:
    import pywhatkit as kit
except:
    os.system("pip install pywhatkit")
    import pywhatkit as kit

try:
    import speedtest
except:
    os.system("pip install speedtest-cli")
    import speedtest

try:
    import wikipedia
except:
    os.system("pip install wikipedia")
    import wikipedia

try:
    from covid import Covid
except:
    os.system("pip install covid")
    from covid import Covid

try:
    from instagramy import InstagramUser as insta
except:
    os.system("pip install instagramy")
    from instagramy import InstagramUser as insta

try:
    from number2words import Number2Words
except:
    os.system("pip install number2words")
    from number2words import Number2Words

try:
    from textblob import TextBlob
except:
    os.system("pip install textblob")
    from textblob import TextBlob

try:
    from translate import Translator
except:
    os.system("pip install translate")
    from translate import Translator


def navigat(input_text):
    return "\n/help"

def sample_responses(input_text,msgSenderData):
    user_message = str(input_text).lower()
    fname = msgSenderData['message']['chat']['first_name']
    lname = msgSenderData['message']['chat']['last_name']
    user_name = msgSenderData['message']['chat']['username']
    mssg = msgSenderData['message']['text']

    f = open("record.txt", "a")
    f.write(f"{fname}, {lname}, {user_name}, {mssg}\n")
    f.close()


    if user_message in ("hello", "hey", "hi","hii"):
        return f"Hey {fname} {lname}... what's going on?"

    if user_message in ("how are you", "how are you?"):
        return f"I'm Fine Dude... How are you {fname}?"

    if user_message in ("who are you", "who are you?"):
        return "I am Aadesh Lokhande's bot"
    
    if user_message in ("chutiya","chutiye","lawde","lawdu","lawda","gandu","bsdk","bhosdike","madarchod","mc","bc",):
        return f"sun be {fname} {lname}\nYahi patak ke Chod Denge...\nNikal madarchod..."

    if user_message in ("time?", "time"):
        now = datetime.now()
        date_time = now.strftime("Time : %H:%M:%S")
        return str(date_time)
    
    if user_message in ("date", "day"):
        now = datetime.now()
        date_time = now.strftime("Date : %d / %m / 20%y")
        return str(date_time)

    if user_message in ("instagram id", "instagram", "instagram username"):
        return "https://www.instagram.com/aadesh_lokhande/"
    
    if user_message in ("net speed","internet speed","download speed",""):
        net = speedtest.Speedtest() 
        dspeed = f"Downloading speed = {int(net.download())/1000000} Mbps\n"
        upspeed = f"Uploading Speed = {int(net.upload())/1000000} Mbps"
        return dspeed+upspeed
    
    if user_message in ("are you okey?","are you ok", "are you okey", "are you ok?"):
        return "Yes, I’m fine, thanks"

    if user_message in ("gm","good morning", "morning"):
        emoji = emojis.encode(":rose:")
        return f"Very Good Morning {fname}{emoji}"
    
    if user_message in ("gn", "good night", "night"):
        return f"Good Night {fname}"
    
    if user_message in ("i love you","i love you so much","i like this bot"):
        heart = emojis.encode(":heart:")
        return f"Thank you to {fname}{heart} "

    if user_message in ("where are you from","where are you from?","where are you","where are you?"):
        return "I Don't like to share my Location"
    
    if user_message in ("what do you do","what do you do?"):
        return "I'm a Python Developer\nhttps://aadeshlokhande.devfolio.io"
    
    if user_message in ("what are you doing?", "what are you doing"):
        return f"learning📚 advance level Python🐍..."
    
    if user_message in ("facebook id", "fb id"):
        return "https://www.facebook.com/aadesh00786/"
    
    if user_message in ("fine","f9","i am fine", "i'm fine", "good", "i'm good", "i am good"):
        return "great...!!! "

    if "wiki" in user_message:
        word = user_message[5:]

        word = str(TextBlob(word).correct())
        try:
            return str(wikipedia.summary(word))
        except:
            return "Wrong Input\ntype: wiki <anytopic>\nExample:- wiki tajmahal"

    if "big" in user_message:
        word = user_message[4:]
        return pyfiglet.figlet_format(word)

    if "emoji" in user_message:
        word = user_message[6:]
        word = str(TextBlob(word).correct())
        emoji = ":"+word+":"
        return emojis.encode(emoji)
    
    if "word in" in user_message:
        number = user_message[8:]
        try:
            number2words = Number2Words(int(number))
            return str(number2words.convert())
        except:
            return "Wrong Input\ntype: word in <any number>\nExample:- word in 12"

    if "url" in user_message:
        url = user_message[4:]

        link = pyshorteners.Shortener().tinyurl.short(str(url))
        return str(link)

    if "table" in user_message:
        a = user_message.split(" ")
        number = a[1]
        table = f"::: Table of {number} :::\n\n"
        for i in range(1,11):
            table = table + f"{int(number)} x {i} = {i*int(number)}\n"
        return table

    if "insta" in user_message:
        username = user_message[6:]

        user = insta(username)
        try:
            idurl = user.profile_picture_url

            id_url = pyshorteners.Shortener().tinyurl.short(idurl)

            data = f"User Name : \t{user.username}\n\nFull Name : \t{user.fullname}\n\nBIO : \t{user.biography}\n\nFollowers : \t{user.number_of_followers}\n\nFollowing : \t{user.number_of_followings}\n\nPosts : \t{user.number_of_posts}\n\nis private : \t{user.is_private}\n\nis verified : \t{user.is_verified} \n\nProfile Pic URL : \t{id_url}\n\nWebsite : {user.website}\n\nProfile pic 👇🏻 👇🏻 👇🏻 👇🏻 👇🏻 👇🏻\n"
            return data
        except:
            return "Wrong Input\ntype: insta <username>\nExample:- insta aadesh_lokhande"

    if "trans" in user_message:
        line = str(user_message[6:])
        text = str(TextBlob(line).correct())
        translator= Translator(to_lang="hi",from_lang='en')
        translation = translator.translate(text)
        return translation

    if "rev" in user_message:
        line = user_message[4:].capitalize()
        return line[::-1]

    if "cap" in user_message:
        line = user_message[4:].upper()
        return line

    if "small" in user_message:
        line = user_message[6:].lower()
        return line

    if "covid" in user_message:
        msg = user_message[6:]
        
        covid = Covid()
        if ("world"==msg) or ("all"==msg):
            case = f"Total Active cases:- {covid.get_total_active_cases()} \nTotal Confirmed cases:- {covid.get_total_confirmed_cases()} \nTotal Recoverd cases:- {covid.get_total_recovered()} \nTotal Death:- {covid.get_total_deaths()}"
            return case
        else:
            msg = str(TextBlob(msg).correct())

            place = covid.get_status_by_country_name(msg)
            data = {
                key : place[key]
                for key in place.keys() and {'confirmed','active','deaths','recovered'}}
            a = f"{msg.capitalize()} Active cases:- {data['active']} \n{msg.capitalize()} Confirmed cases:- {data['confirmed']} \n{msg.capitalize()} Recoverd cases:- {data['recovered']} \n{msg.capitalize()} Total Death:- {data['deaths']}"
            return a

    if "ytplay" in user_message:
        topic = user_message[7:]
        kit.playonyt(topic)
        return "Playing"

    if "find" in user_message:
        msg = user_message[5:]
        kit.search(msg) 
    
    if "bitcoin"==user_message:
        price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
        return f"Current Bitcoin Price Is {str(price)} US Dollers"
    
    if "calc" in user_message:
        eq = user_message[5:]
        try:
            return "Answer = "+str(eval(eq))
        except:
            return "There is problem in your equation. check and try again\nThis is a simple Calculator"

    if "month" in user_message:
        msg = user_message.split(" ")
        try:
            return calendar.month(int(msg[2]),int(msg[1]))
        except:
            return "Wrong Input\nType: month <month> <year>\nExample: month 9 1997"

    if "resume" in user_message:
        return "tinyurl.com/AadeshResume"
        



    return "I don't understand you."



    # cd Documents/MyProjects/PythonData/python\ Practice/telagramBot/
# cd Documents/MyProjects/PythonData/python\ Practice/telagramBot/ && python3 telegramBot.py
