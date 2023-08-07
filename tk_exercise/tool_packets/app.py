from flask import Flask,url_for,session, redirect, flash,render_template,request



app = Flask(__name__)


@app.route("/", methods = ['GET','POST']) 
def home():

    return render_template("home.html")

@app.route("/toIco", methods = ['GET','POST']) 
def toIco():
    if request.method == "POST":
        uploadimage = request.files.getlist("uploadimage")
        file = uploadimage[0]
        file.save("./static/toicoimg/icoimg.ico")
        print(uploadimage,type(uploadimage))

    return render_template("toIco.html")

if __name__ == '__main__':
    app.run(debug=True)