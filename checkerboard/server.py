from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard4(x = 8, y = 8, color1 = 'lawngreen', color2 = 'deeppink'):
    output = []
    for i in range(0, x):
        temp = []
        for j in range(0, y):
            temp.append((i + j) % 2)
        output.append(temp)
    return render_template("checkerboard.html", output = output, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)