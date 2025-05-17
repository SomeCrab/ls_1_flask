from flask import Flask, render_template , request, jsonify, session
from config import SECRET_KEY, HOST, PORT
from uuid import uuid4

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/v1/home', methods=['GET'])
def home_route():
    return jsonify({
        'message': 'JSON API endpoint',
        'status': 'success'
    })


@app.route('/profile/<string:username>')
def get_profile(username):
    referrer = request.referrer
    if 'user_uuid' not in session:
        session['user_uuid'] = str(uuid4())

    return render_template(
        'profile.html',
        username=username,
        user_uuid=session['user_uuid'],
        referrer=referrer
        )


@app.route('/profile_uuid/<uuid:user_uuid>')
def get_profile_uuid(user_uuid):
    referrer = request.referrer

    return render_template(
        'uuid.html',
        user_uuid=user_uuid,
        referrer=referrer
        )


@app.route('/number/<float:number>')
def get_number(number):
    type_n = str(type(number))
    print(type_n)
    return f'<h1>Number: {number} <br>Type: {type_n}</h1>'


@app.route('/send_password', methods=['POST'])
def get_password():
    password = request.form.get('password')
    print("Password: ", password)
    return f'This is secret password: "{password}"'


if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT,
        debug=True
        )