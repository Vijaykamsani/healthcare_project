from flask import Flask, jsonify 
app = Flask(__name__)
@app.route("/")
def home():
    return("Hello Divya")
if __name__== '__main__':
    app.run()