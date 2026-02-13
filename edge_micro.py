import asyncio
import edge_tts
import os

async def generate_audio() -> None:
    os.makedirs("output",exist_ok=True)

    text="Hello yash,this is high quality neural text to speech running " \
    "without gpu."

    communicate = edge_tts.Communicate(text,"en-US-AriaNeural")
    #communicate = egde_tts.Communicate(text,"hi-IN-SwaraNeural")

    await communicate.save("output/edge_output_en.mp3")

    print("Audio Generated succesfully")

asyncio.run(generate_audio())