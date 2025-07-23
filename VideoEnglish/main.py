from PIL import Image, ImageFont, ImageDraw
from moviepy.editor import *
from Tech_In_Seconds import agl
import textwrap
import pyttsx3
from mutagen.wave import WAVE
import shutil

OBFont = 'Data/Oswald-Bold.ttf'
a = 4

word = input("enter a word = ").lower()

try:
    line = agl.mean(word)[0]
    if(len(line) <= 500):
    ################## words img ####################
        img = Image.open('Data/img.png')
        I1 = ImageDraw.Draw(img)
        I1.text((200+a, 240+a), "Word : ", fill=(0, 0, 255),font=ImageFont.truetype(OBFont, 120))
        I1.text((200, 240), "Word : ", fill=(52, 237, 225),font=ImageFont.truetype(OBFont, 120))
        I1.text((300+a, 400+a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300-a, 400-a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300+a, 400-a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300-a, 400+a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300, 400), word.capitalize(), fill=(255, 255, 255),font=ImageFont.truetype(OBFont, 90))
        img.save(f"Data/WordImg.png")

    ################## mean Img ####################

        img = Image.open('Data\img.png')
        I1 = ImageDraw.Draw(img)
        I1.text((200+a, 240+a), "Word : ", fill=(0, 0, 255),font=ImageFont.truetype(OBFont, 120))
        I1.text((200, 240), "Word : ", fill=(52, 237, 225),font=ImageFont.truetype(OBFont, 120))
        I1.text((300+a, 400+a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300-a, 400-a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300+a, 400-a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300-a, 400+a), word.capitalize(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 90))
        I1.text((300, 400), word.capitalize(), fill=(255, 255, 255),font=ImageFont.truetype(OBFont, 90))
        I1.text((200+a, 530+a), "Mean : ", fill=(0, 0, 225),font=ImageFont.truetype(OBFont, 120))
        I1.text((200, 530), "Mean : ", fill=(52, 237, 225),font=ImageFont.truetype(OBFont, 120))
        
        wrapper = textwrap.TextWrapper(width=70)
        word_list = wrapper.wrap(text=line)
        y = 700
        for i in word_list:
            I1.text((300+a, y+a),text=i, fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 70))
            I1.text((300-a, y-a),text=i, fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 70))
            I1.text((300+a, y-a),text=i, fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 70))
            I1.text((300-a, y+a),text=i, fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 70))
            I1.text((300, y),text=i, fill=(255, 255, 255),font=ImageFont.truetype(OBFont, 70))
            y = y + 80
        img.save(f"Data/MeanImg.png")

    ################## audio ####################
        text = f"""Today, let's explore a new word: {word}. This intriguing term encompasses a world of meaning, and it's a word that evokes curiosity and invites us to delve deeper into its significance. Let's unravel its beauty and uncover the richness of its definition... the meaning of {word} is {line}. if you like this video please like share and subscribe to our channel tech in seconds english"""        
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        engine.setProperty('volume', 1)
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[0].id)
        engine.save_to_file(text, f'Data/audio.mp3')
        engine.runAndWait()
        
    ################## Video ####################

        audio = WAVE(f"Data/audio.mp3")
        audio_info = audio.info
        length = int(audio_info.length)

        wordImg = ImageClip("Data/WordImg.png").set_duration(18)
        meanImg = ImageClip('Data/MeanImg.png').set_duration(length-24)
        endImg = ImageClip(f'Data/endpage.png').set_duration(6)

        video = concatenate([ wordImg,meanImg,endImg], method="compose")
        video.write_videofile(f'Data/video.mp4', fps=5)

        clip = VideoFileClip(f"Data/video.mp4")
        audioclip = AudioFileClip(f"Data/audio.mp3")
        videoclip = clip.set_audio(audioclip)
        videoclip.ipython_display()

        source = "__temp__.mp4"
        destination = f"aadesh.mp4"
        shutil.move(source, destination)

        ################## Thumbnail ####################

        img = Image.open('Data/img.png')
        I1 = ImageDraw.Draw(img)

        I1.text((200+a, 240+a), "WHAT IS", fill=(0, 0, 255),font=ImageFont.truetype(OBFont, 200))
        I1.text((200, 240), "WHAT IS", fill=(52, 237, 225),font=ImageFont.truetype(OBFont, 200))

        I1.text((200+a, 440+a), f"{word} ?".upper(), fill=(255, 0, 0),font=ImageFont.truetype(OBFont, 200))
        I1.text((200, 440), f"{word} ?".upper(), fill=(255, 255, 255),font=ImageFont.truetype(OBFont, 200))

        img.save(f"thumbnail.png")
except:
    print(f"Error : {word} meaning is not available".upper())
