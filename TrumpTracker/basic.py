import fetcher, parser
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['GET'])
def fetch():
    fetcher.romanov()
    data = parser.banner()
    return data

if __name__ == "__main__":
    app.run(debug=True)

# Git commit