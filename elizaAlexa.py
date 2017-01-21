import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

import eliza as ez

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
f = open('templates.yaml','w')

@ask.launch
def begin_session():
	start_msg = render_template('start')
	return question(start_msg)

@ask.intent("ResponseIntent",convert={'answer':str})
def start_conversation(answer):
	session.attributes['answers']=answer
	eliza_response = ez.analyze(session.attributes['answers'])
	f.write("curr_response: "+eliza_response)
	curr_response_msg = render_template('curr_response')
	return question(curr_response_msg)

if __name__=='__main__':
	app.run(debug=True)