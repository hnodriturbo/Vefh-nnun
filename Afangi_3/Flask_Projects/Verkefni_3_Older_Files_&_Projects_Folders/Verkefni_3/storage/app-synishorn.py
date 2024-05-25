from flask import Flask, render_template, json
import urllib.request
import certifi # þurfið að gera -> pip install certifi
import ssl 
certifi_context = ssl.create_default_context(cafile=certifi.where()) 

app = Flask(__name__)

# route sem keyrir fyrirspurn sem skilar 20 þáttum á fyrstu síðu (page=1) á API hjá themoviedb.org
@app.route('/')
def index():

    # hér fyrir neðan þarftu að setja þinn api_key í staðinn fyrir xxx.  Þú sækir api_key á https://www.themoviedb.org/settings/api eftir að þú hefur loggað þig inn
    with urllib.request.urlopen("https://api.themoviedb.org/3/discover/tv?api_key=xxx", context=certifi_context ) as url:
        gogn = json.loads(url.read().decode())
    
    print(gogn) # prentum í command glugga bara til að ath. hvort við fáum ekki API gögnin frá themoviedb.org

    return "Prófum að sækja gögn úr API hjá themoviedb.org, ath að hér ættir þú að vera að nota render_template fallið"

if __name__ == "__main__":
    app.run()