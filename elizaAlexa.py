import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

import eliza as ez

import datetime as dt

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
name = "Archit"
f = open("Transcript_"+name+".txt",'a')
f.write(str(dt.datetime.now())+"\n\n")

@ask.launch
def begin_session():
	start_msg = render_template('start')
	f.write("Eliza: "+start_msg+"\n")
	return question(start_msg)

@ask.intent("ResponseIntent",convert={'answer':str})
def start_conversation(answer):
	#f = open('templates.yaml','a')
	session.attributes['answers'] = answer
	f.write("You: "+answer+"\n")
	eliza_response = ez.analyze(session.attributes['answers'])
	#f.write("curr_response: " + eliza_response)
	#f.close()
	curr_response_msg = str(eliza_response)
	f.write("Eliza: "+curr_response_msg+"\n")
	return question(curr_response_msg)

if __name__=='__main__':
	app.run(debug=True)
	f.write("\n\n")
	f.close()
