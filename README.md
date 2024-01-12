# REST-TTS-Dockerfize
TTS REST API wrapper with FastAPI and Docker, for your text-to-speech needs🤖

## Installation
1. To build image, run `docker build . --tag my/tts-api`
1. To run image, run`docker run -d -p 7861:7861 -v ./audio:/code/audio -v ./tts:/root/.local/share/tts --name tts-api my/tts-api`
1. Make sure to have the `-v` volume parameter to avoid redownloading models.
1. For CPU only, use `ghcr.io/coqui-ai/tts-cpu`, for GPU use `ghcr.io/coqui-ai/tts` as Dockerfile base image.
1. Go to `http://127.0.0.1:7861/api/` to check the app

## USAGE
* to convert text to speech, use the `POST` endpoint `/api/tts/`
with payload of `{message:"read this",name:"arnold"}`. `message` is the text to be read and `name` is the sampling voice to be cloned. this returns the filename of the audio
* to read back converted speech, use the `GET` endpoint `/api/voice/`
with audio filename set a query params `name`  e.g. `.../api/voice?name=sample01.wav`