from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Pipeline</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #000000);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                color: white;
                font-family: 'Courier New', Courier, monospace;
            }
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            h1 {
                font-size: 4rem;
                text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
                margin-bottom: 10px;
                text-align: center;
            }
            h2 {
                font-size: 2rem;
                color: #00ffcc;
                margin-top: 0;
                text-align: center;
            }
            .badge {
                margin-top: 30px;
                padding: 15px 30px;
                background: rgba(255,255,255,0.1);
                border: 1px solid #00ffcc;
                border-radius: 5px;
                box-shadow: 0 0 10px #00ffcc;
                animation: pulse 2s infinite;
                font-weight: bold;
                letter-spacing: 2px;
            }
            @keyframes pulse {
                0% { box-shadow: 0 0 5px #00ffcc; }
                50% { box-shadow: 0 0 20px #00ffcc; }
                100% { box-shadow: 0 0 5px #00ffcc; }
            }
        </style>
    </head>
    <body>
        <h1>Gaade Libun Kumar</h1>
        <h2>DevOps Engineer</h2>
        <div class="badge">
            🚀 SECURED DEVSECOPS PIPELINE IS LIVE
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
