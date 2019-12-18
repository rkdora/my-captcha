from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route('/', methods=['GET', 'POST'])
def index():

    # img_type = "inverse"

    img_type = "advs"

    if request.method == 'POST':
        num = request.form['num']
        ans = "認証に失敗しました"
        if is_valid_num(num) and (session['label_num'] == int(num)):
            ans = "認証に成功しました"

        session['label_num'] = random.randint(0,9)
        return render_template('index.html', ans=ans, img_type=img_type)
    else:
        session['label_num'] = random.randint(0,9)
        return render_template('index.html', img_type=img_type)

def is_valid_num(n):
    return len(n) == 1 and n.isdecimal()

if __name__ == "__main__":
    app.run()
