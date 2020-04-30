import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''



<!DOCTYPE html>
<html>
<title>Fish Finder</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">

<style>

body,h1 {font-family: "Raleway", sans-serif}
body, html {height: 100%}

.bgimg {
  background-image: url('https://garibaldicharters.com/wp-content/uploads/2016/07/water-background.jpg');
  min-height: 100%;
  background-position: center;
  background-size: cover;
}

.boxed {
  width: 300px;
  background: rgba(50,50 ,75, 0.7);
  border-radius: 5px;
  padding: 50px;
  margin: 20px;
}
</style>
<body>

<div class="bgimg w3-display-container w3-animate-opacity w3-text-white">

  <!--Title block-->
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">Fish Finder</h1>
    <hr class="w3-border-white" style="margin:auto;width:60%">
    <br>

    <!--submit form block-->
    <div class="boxed">
      <form>
        <label for="myfile">Click below to upload your fish photo:</label>
        <br>
        <br>
        <input type="file" id="myfile" name="file">
        <input type=submit value=Upload>
      </form>
    </div>

  </div>

  <div class="w3-display-bottomleft w3-padding-large w3-xlarge w3-text-white">
      Sean Mackay, Benjamin Conomos, Justin Henderson
  </div>
</div>

</body>
</html>
