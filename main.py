from flask import Flask, render_template, url_for, request

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

if __name__ == '__main__':
    #app.run(host = '2409:4043:2203:d0ff:40a4:30d5:aa1e:9f32')
    app.run(debug = True, host = '2409:4043:2e02:2a22:cdfe:cb12:4ce5:25bb')