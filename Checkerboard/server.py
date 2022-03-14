from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def four():
    return render_template("4.html")


if __name__=="__main__":
    app.run(debug=True)

    