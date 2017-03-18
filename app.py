from flask import Flask
import urllib
import sys
import requests


app = Flask(__name__)
repoUrl = sys.argv[1]
owner = repoUrl.split('/')[3]
repo = repoUrl.split('/')[4]
git_url ="http://api.github.com/repos"

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<filename>")
def getrepo(filename):
	headers = {'Accept': 'application/vnd.github.v3.raw'}
	content = requests.get(git_url+"/"+owner+"/"+repo+"/contents/"+filename,headers=headers)
	return content.content

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


