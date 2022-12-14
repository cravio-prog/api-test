from flask import Flask,render_template,request,redirect,url_for
from flask import make_response
import jsonify
import requests
from simple_geoip import GeoIP


app = Flask(__name__)

@app.route("/api/<nome>",methods=["GET"])
def apiproc(nome=None):
    try:
        if request.method=="POST":
            return "POST API NOT DEFINED"
        elif request.method=="GET":
            print("richiesta POST")
            print("nome",nome)
            if nome== "geotest":
                try:
                    geoip = GeoIP("at_IbsACgQWCfaTLCkKT0s6Xg2nxBcbW")
                    # data = geoip.lookup(request.remote_addr)
                    ind = str(request.access_route[-1])

                    if ":" in ind:
                        ind = ind[:ind.find(":",0)]

                    data = geoip.lookup(ind)
                except ConnectionError:
                    return "ERRORE CONNECTIONERROR"
                    # If you get here, it means you were unable to reach the geoipify
                    # service, most likely because of a network error on your end.

                return data

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
def staticfeed():
    try:
        f=open("templates/staticfeed.html","r")
        s = f.read()
#        s = htmlmin.minify(s)
        response = make_response(s)
        response.headers.set('Content-Type', 'application/rss+xml')
        f.close()
        return response

    except Exception as e:
        print(e)
        return "ERR - " + str(e)

@app.route("/staticfeed2",methods=["GET"])
def staticfeed2():
    try:
        f=open("templates/staticfeed2.html","r")
        response = make_response(f.read())
        response.headers.set('Content-Type', 'application/rss+xml')
        f.close()
        return response

    except Exception as e:
            print(e)
            return "ERR - " + str(e)


@app.route("/dailyprivatenew",methods=["GET"])
def dailyprivatenew():
    try:
        email_get=request.args.get('mail', '')
        #time.sleep(0.05)
        response = make_response(requests.get('https://www.we-wealth.com/api/sitecore/mailup/dailyprivatenew?mail='+email_get).text)
        response.headers.set('Content-Type', 'application/rss+xml')
        return response        


    except Exception as e:
            print(e)
            return "ERR - " + str(e)

@app.route("/dailyprivate",methods=["GET"])
def dailyprivate():
    try:
        email_get=request.args.get('mail', '')
        #time.sleep(0.05)

        sitecore_response = requests.get('https://www.we-wealth.com/api/sitecore/mailup/dailyprivate?mail='+email_get)
        response = make_response(sitecore_response.text)
#        response.headers = sitecore_response.headers
        response.headers.set('Content-Type', 'application/rss+xml')
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