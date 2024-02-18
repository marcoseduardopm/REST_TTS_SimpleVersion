from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime
import torch
import re
from TTS.api import TTS


#print(TTS().list_models())

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: " + device)
tts = TTS("xtts_v2.0.2").to(device)
#tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
#wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# Text to speech to a file
#tts.tts_to_file(text="Hello world!", speaker_wav="audio/voices/default.wav", language="en", file_path="output.wav")

#Based on https://github.com/rsandagon/REST_TTS_Dockerized
app = FastAPI(
    title="Simple REST TTS",
    description="Simple TTS REST API wrapper with FastAPI, based on https://github.com/rsandagon/REST_TTS_Dockerized",
    summary="TTS REST API",
    version="0.0.1",
    #terms_of_service="https://github.com/rsandagon/REST_TTS_Dockerized/README.md",
    contact={
        "name": "marcoseduardopm",
        "url": "https://github.com/marcoseduardopm",
        "email": "marcoseduardopm@hotmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

class Item(BaseModel):
    name: str
    message: str 

def remove_between_asterisks(text):
  pattern = r"\*.*?\*"
  return re.sub(pattern, "", text)

@app.get("/")
def read_root():
    return {"Hello": "I'm alive!"}


@app.get(
    path="/api/snd"
)
async def post_media_file(name:str='default'):
    return FileResponse("audio/outputs/"+name, media_type="audio/mpeg")

@app.post("/api/tts")
async def post_tts(item: Item):
    now = datetime.now()
    nowstr = now.strftime("%m%d%Y_%H%M%S")
    outname = item.name+nowstr+".wav"
    srcname = item.name+".wav"

    tts.tts_to_file(text=remove_between_asterisks(item.message), speaker_wav="audio/voices/"+srcname, language="en", file_path="audio/outputs/"+outname)
    # or return FileResponse of the wav if machine is fast enough
    return FileResponse("audio/outputs/"+outname, media_type="audio/mpeg")
    #return {"file":outname}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)