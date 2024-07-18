from flask import Flask, render_template, request, redirect, url_for, session
import game

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
@app.route('/')
def index():
    session['level'] = 1  # Reset level to 1 every time the page is refreshed
    level_info = game.get_level_info(session['level'])
    return render_template('index.html', level_info=level_info)

@app.route('/submit_code', methods=['POST'])
def submit_code():
    user_code = request.form['code']
    level = session.get('level', 1)
    result, success = game.check_code(level, user_code)
    if success:
        session['level'] += 1
    return render_template('index.html', result=result, level_info=game.get_level_info(session['level']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
