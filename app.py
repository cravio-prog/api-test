from flask import Flask,render_template,request,redirect,url_for
import json
from flask import make_response

app = Flask(__name__)

@app.route("/api/<nome>",methods=["GET"])
def apiproc(nome=None):
    try:
        if request.method=="POST":
            return "POST API NOT DEFINED"
        elif request.method=="GET":
            print("richiesta POST")
            print("nome",nome)
            if nome== "mailfeed":
                email_get=request.args.get('mail', '')
                if email_get != "":
#                return render_template('output.html', columns=columns, row_data=email_serach[0], zip=zip)
                    return render_template("mailfeed.html",email=email_get)
                else:
                    return "ERROR"
            if nome== "article":
                email_get=request.args.get('mail', '')
#                return render_template('output.html', columns=columns, row_data=email_serach[0], zip=zip)
                return render_template("article.html",email=email_get)

            if nome== "staticfeed":
                return render_template("staticfeed.html")
            if nome== "staticfeed2":

                return render_template("staticfeed2.html")

    except Exception as e:
            print(e)
            return "ERR - " + str(e)

@app.route("/staticfeed",methods=["GET"])
def staticfeed(nome=None):
    try:
        f=open("templates/staticfeed.html","r")
        response = make_response(f.read())
        response.headers.set('Content-Type', 'application/rss+xml')
        f.close()
        return response

    except Exception as e:
        print(e)
        return "ERR - " + str(e)

@app.route("/staticfeed2",methods=["GET"])
def staticfeed2(nome=None):
    try:
        f=open("templates/staticfeed2.html","r")
        response = make_response(f.read())
        response.headers.set('Content-Type', 'application/rss+xml')
        f.close()
        return response

    except Exception as e:
            print(e)
            return "ERR - " + str(e)

@app.route('/')
def index():
    return "<p>Hello, World!</p>"


'''    
@app.route("/home")
@auth.login_required
def home():
    return render_template("home.html")
'''

if __name__ == '__main__':
    print("__main__")
    app.run()