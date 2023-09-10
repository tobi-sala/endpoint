from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/path')

def index():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    date = datetime.datetime.utcnow()

    data = {
        "slack_name": "tobiloba_salaudeen",
        "current_day" : date.strftime("%A"),
        "utc_time" : date,
        "track" : "backend",
        "github_file_url" : "https://github.com/tobi-sala/endpoint/blob/main/endpoint.ext",
        "github_repo_url" : "https://github.com/tobi-sala/endpoint.git",
        "status_code" : 200
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run()