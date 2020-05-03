import os
#import magic
import urllib.request
#from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

from flask import Flask

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
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
      <form method="post" action="/" enctype="multipart/form-data">
	      <dl>
	  		<p>
	  			<input type="file" name="file" autocomplete="off" required>
	  		</p>
	      </dl>
	      <p>
	  		<input type="submit" value="Submit">
	  	</p>
		</form>
    </div>

  </div>

  <div class="w3-display-bottomleft w3-padding-large w3-xlarge w3-text-white">
      Sean Mackay, Benjamin Conomos, Justin Henderson
  </div>
</div>

</body>
</html>
'''


@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
