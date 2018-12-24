import fetcher, parser, time
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')
        #"Elapsed time: " + str(e) + "\nCounter: " + str(c)

@app.route('/fetch', methods=['GET'])
def fetch():
    fetcher.romanov()
    print('Fetching done')
    data = parser.banner()
    print('Parsing done!')
    return data

if __name__ == "__main__":
    app.run(debug=True)
