from flask import Flask,request
from flask import render_template
import TrieLogic.Trie as searchEngine
import json 
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def home():
    return render_template("main.html")

@app.route("/search", methods=['POST','GET'])
def searchLogic():
    global TrieRootNnode
    
    if request.method == "POST":
        search  = request.json['search']
        
        res = TrieRootNnode.searchQueries(search)
        jsonObj =  {"result":res}
        
        return json.dumps(jsonObj)
    return "cant support get request"



if __name__ == "__main__":
    global TrieRootNnode
    TrieRootNnode = searchEngine.BuildTrie()
  # print(TrieRootNnode.searchQueries("yukesh"))
    
    app.run(debug=True)