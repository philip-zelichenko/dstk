from flask import Flask, render_template, Response
import time

app = Flask(__name__)

y = 1.5

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/progress')
def progress():
    def generate():
        x = 0

        while x <= 100:
            yield "data:" + str(x) + "\n\n"
            x = x + 1
            time.sleep(y)

    return Response(generate(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run()