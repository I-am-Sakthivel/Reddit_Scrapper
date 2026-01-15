# /// script
# dependencies = [
#   "praw",
#    "python-dotenv",
#    "flask"
# ]
# ///

from scrapper import scrape
from flask import Flask,render_template,request,redirect,send_file

app=Flask(__name__)

@app.route('/',methods=['GET'])
def download():
    return render_template("index.html")

@app.route('/csv')
def csv_down():
    data=request.args
    path=scrape(data['subreddit'])
    if path =="Sub Does not exist":
        return redirect('/dne')
    return send_file(path,as_attachment=True)

@app.route('/dne')
def dne():
    return render_template('dne.html')

if __name__=='__main__':
    app.run()