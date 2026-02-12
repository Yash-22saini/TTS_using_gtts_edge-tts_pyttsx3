from gtts import gTTS
import os

os.makedirs('output', exist_ok=True)

# text = "Hi Yash your model gtts is working perfectly."

text="तेरी आँखों की बात हो तो पैमाना याद आया, उल्फ़त जो याद आयी तो मैखाना याद आया! दुनिया वाले करते है इश्क़ और गम की बातें, जब भी देखा शमा को तो परवाना याद आया! ज़माने भर की बातो में कही भूल न जाना हमें, अक्सर ख्वाबों में तेरा मुस्कुराना याद आया! "

tts = gTTS(text=text, lang='hi')

filepath = "output/output_hi.mp3"

tts.save(filepath)

print("audio saved successfully at : ", filepath)