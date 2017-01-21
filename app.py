#!flask/bin/python
from flask import Flask,request,render_template,jsonify
#import tweet_response

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_query():
    if 'geography' in request.args:
        print request.args["geography"]
        return "You typed in geography"

@app.errorhandler(404)
def not_found_404(error):
    return '404.html'

@app.errorhandler(500)
def not_found_500(error):
    return '500.html'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
