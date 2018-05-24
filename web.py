from flask import Flask
app = Flask(__name__)

@app.route('/')
de index():
  return 'hello, world'
