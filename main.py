from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/welcome", methods=['GET'])
def display():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


@app.route("/signup", methods=['POST'])
def signup_validate():
    if request.method == 'POST':
        password = request.form['password']

        username = request.form['username']

        verification = request.form['verification']
        
        email = request.form['email']

        email_error = ""

        user_error = ""

        pass_error = ""

        verification_error = ""


        if len(password) < 3 or len(password) > 20 or " " in password:
            pass_error = "That's not a valid password"
            password = ""


        if password != verification:
            verification_error = "The passwords do not match"
            verification = ""

        if len(username) < 3 or len(username) > 20 or " " in username:
            user_error = "That's not a valid username"
            username = ""

        if "@" not in email or "." not in email:
            email_error = "That is not a valid email"
            email = ""

        if not pass_error and not verification_error and not user_error and not email_error:
            return redirect('/welcome?username=' + username)
        else:
            template = jinja_env.get_template('index.html')
            return template.render(user_error=user_error, pass_error=pass_error,
                                verification_error=verification_error, username=username,
                                verification=verification, password=password)
    else:
        return render_template('index.html')


app.run()
