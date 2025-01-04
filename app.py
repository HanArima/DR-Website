from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("base.html")

@app.route("/detect")
def detect():
  return render_template("detect.html")

@app.route("/revisit")
def revisit():
  return render_template("revisit.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)