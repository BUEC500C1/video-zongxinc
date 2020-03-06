

from flask import Flask, request, render_template, send_file
import converter

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text. upper()
    converter.compressVideo([processed_text],10)
    return processed_text

@app.route('/file-download/')
def file_download():
    return render_template('file.html')

@app.route('/return-file/')
def return_file():
    return send_file('v_@LITWORKS.avi')


if __name__ == '__main__':
    app.run(debug=True)