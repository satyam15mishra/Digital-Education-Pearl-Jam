from flask import Flask, render_template, url_for, request
from text_speech import mytts

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
	global topic_name
	topic_name = request.form['topic_name']
	return render_template('page1.html')

@app.route('/report_page_2', methods = ['GET', 'POST'])
def report_page_2():
	language = request.form['language']
	mytts(topic_name, language)
	return render_template('done.html', language = language, topic_name = topic_name)

@app.route('/text_to_speech', methods = ['GET', 'POST'])
def text_to_speech():
	return render_template('text_to_speech.html')


if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug = True, host = '2409:4043:2e02:2a22:cdfe:cb12:4ce5:25bb')
