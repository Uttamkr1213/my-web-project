from flask import Flask, render_template, jsonify
topics_dict= [
  {
  "title":"Ladakh",
  "description":"Fast by Funsuk",
  "posted_by":"Rajesh"
  },
  {
  "title":"Forest",
  "description":"Forest cutting in MP"
  }
  {
    "title":"Election 2024",
    "description":"Do BJP will win election 2024"
  }
]

app = Flask(__name__)
@app.route('/')
def hello_world():
  return render_template('home.html',topics=topics_dict)
@app.route('/api/topics')
def list_topics():
  return jsonify(topics_dict)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)


  

  