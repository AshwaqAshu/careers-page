from flask import Flask, jsonify, render_template

app = Flask(__name__)

data = [{'title': 'hello'}]


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/api/json')
def json():
  return jsonify(data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
