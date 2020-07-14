from flask import Flask,request,jsonify
import random
import json 
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_query_string():
    try:
        f = open('intents.json',) 
        data = json.load(f) 
        f.close() 
        query = request.args.getlist('key')[0]

        for i in data["intents"]:
            if query in i['patterns']:
                return random.choice(i['responses'])
        else:
            raise("Bad Input Error")    
    except :
        return "Bad Input Error"

if __name__ == '__main__':
    app.run(debug=True)