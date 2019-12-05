from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form['num']
        ans = "認証に失敗しました"
        if is_valid_num(num) and (session['label_num'] == int(num)):
            ans = "認証に成功しました"

        session['label_num'] = random.randint(0,9)
        return render_template('index.html', ans=ans)
    else:
        session['label_num'] = random.randint(0,9)
        return render_template('index.html')

def is_valid_num(n):
    return len(n) == 1 and n.isdecimal()

if __name__ == "__main__":
    app.run()
