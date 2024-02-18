# REST-TTS-SimpleVersion

This repository is a Fork of the (https://github.com/rsandagon/REST_TTS_Dockerized), removing the Docker part in case you need to run without a docker. 
This is a Toqui-ai TTS REST API wrapper with FastAPI.


## Installation
1. Install PyTorch using `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`. For more information, please see https://pytorch.org/.
1. Install other requirements using `pip3 install --no-cache-dir --upgrade -r requirements.txt`
1. To start the service, use `python ./main.py`
1. For more information about the available REST services, please see `http://127.0.0.1:8000/docs/`.


## USAGE
1. To convert text to speech, use the `POST` endpoint `/api/tts/` with payload of `{message:"Hello World!",name:"arnold"}`. `message` is the text to be read and `name` is the sampling voice to be cloned. The audio will be returned.
1. More voices can be included adding files to 'audio/voices'.
1. You can also test it through `http://127.0.0.1:8000/docs/`.
1. All generated audio is saved in `audio/outputs` folder with the file name `<sample>_<timestamp>`.