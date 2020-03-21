from flask import Flask, render_template, url_for, request, session
import os
from trans import converthindi, convertenglish
app.secret_key = os.urandom(16)


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
	topic_name = request.form['topic_name']
	return render_template('page1.html', topic_name = topic_name)

@app.route('/report_page_2')
def report_page_2():
	return render_template('page2.html')

@app.route("/", methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route("/ans", methods=['GET','POST'])
def index():
	data = request.form['trans']
	converthindi(data)
	return (render_template('ans.html', answer=converthindi(data),data=data))

@app.route("/hindi", methods=['GET','POST'])
def hindi():
	data = request.form['trans']
	convertenglish(data)
	return (render_template('hindi.html', answer=convertenglish(data), data=data))


if __name__ == '__main__':
    #app.run(host = '2409:4043:2203:d0ff:40a4:30d5:aa1e:9f32')
    app.run(debug = True, host = '2409:4043:2e02:2a22:cdfe:cb12:4ce5:25bb')
