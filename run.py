from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def start():
	return render_template('index.html')

@app.route('/<filename>',methods=['GET', 'POST'])
def serve_static(filename):
    return send_from_directory('templates',filename)

@app.route('/assets/<filename>',methods=['GET', 'POST'])
def serve_icon(filename):
    return send_from_directory('templates',filename)