from gtts import gTTS

def mytts(text, language = 'en-us'):
	tts = gTTS(text, lang = language)
	tts_file_name = 'hacknitr.mp3'
	path = 'static/'+tts_file_name
	tts.save(path)
