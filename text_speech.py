from gtts import gTTS

def mytts(text, language = 'en-us'):
	tts = gTTS(text, lang = language)
	#tts_file_name = str(text)+'.mp3'
	tts_file_name = 'song1.mp3'
	path = 'static/'+tts_file_name
	tts.save(path)