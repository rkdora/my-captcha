from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    label_num = random.randint(0,9)
    img_num = 0
    return render_template('index.html', label_num=label_num, img_num=img_num)

if __name__ == "__main__":
    app.run()
