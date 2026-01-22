from flask import Flask, render_template, request, send_file
from rembg import remove
import uuid
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['PROCESSED_FOLDER'] = 'static/processed/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        filename = image_file.filename
        ex = os.path.splitext(filename)[1]
        id = str(uuid.uuid4())
        new_filename = f"{id}{ex}"
        path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        image_file.save(path)

        new_path = os.path.join(app.config['PROCESSED_FOLDER'], new_filename)

        with open(path, 'rb') as oi:
            with open(new_path, 'wb') as ni:
                input = oi.read()
                output = remove(input)
                ni.write(output)

        return render_template('index.html', image=new_filename)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)