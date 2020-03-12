from flask import Flask, render_template

app = Flask(__name__)

counter = -1

@app.route('/')
def index():
  global counter
  counter += 1
  return render_template('index.html', count=str(counter))

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

