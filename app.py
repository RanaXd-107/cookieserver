from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('visitor', 'ZainXdVisitor', max_age=60*60*24*7)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
