import os

import requests
import json
import pprint

def getProfile(text):
    url = "https://gateway.watsonplatform.net/personality-insights/api"
    username = "ae94b75a-bc86-4dc3-babe-715d6bc1a21e"
    password = "Vm8xAgu0KVZY"

    """Returns the profile by doing a POST to /v2/profile with text"""
    if url is None:
        raise Exception("No Personality Insights service is bound to this app")

    response = requests.post(url + "/v2/profile",auth=(username,password),headers={"content-type": "text/plain"},data=text)
    try:
        return json.loads(response.text)
    except:
        raise Exception("Error processing the request, HTTP: %d" %response.status_code)

text = "Vice President Johnson, Mr. Speaker, Mr. Chief Justice, President Eisenhower,\
Vice President Nixon, President Truman, Reverend Clergy, fellow citizens:\
\
We observe today not a victory of party but a celebration of freedom --\
symbolizing an end as well as a beginning -- signifying renewal as well as\
change. For I have sworn before you and Almighty God the same solemn oath our\
forbears prescribed nearly a century and three-quarters ago.\
\
The world is very different now. For man holds in his mortal hands the power\
to abolish all forms of human poverty and all forms of human life. And yet\
the same revolutionary beliefs for which our forebears fought are still at\
issue around the globe -- the belief that the rights of man come not from the\
generosity of the state but from the hand of God.\
\
We dare not forget today that we are the heirs of that first revolution. Let\
the word go forth from this time and place, to friend and foe alike, that the\
torch has been passed to a new generation of Americans -- born in this century,\
tempered by war, disciplined by a hard and bitter peace, proud of our ancient\
heritage -- and unwilling to witness or permit the slow undoing of those human\
rights to which this nation has always been committed, and to which we are\
committed today at home and around the world.\
\
Let every nation know, whether it wishes us well or ill, that we shall pay\
any price, bear any burden, meet any hardship, support any friend, oppose\
any foe to assure the survival and the success of liberty.\
\
This much we pledge -- and more.\
\
To those old allies whose cultural and spiritual origins we share, we pledge\
the loyalty of faithful friends. United there is little we cannot do in a host\
of cooperative ventures. Divided there is little we can do -- for we dare not\
meet a powerful challenge at odds and split asunder.\
\
To those new states whom we welcome to the ranks of the free, we pledge our\
word that one form of colonial control shall not have passed away merely to\
be replaced by a far more iron tyranny. We shall not always expect to find\
them supporting our view. But we shall always hope to find them strongly\
supporting their own freedom -- and to remember that, in the past, those who\
foolishly sought power by riding the back of the tiger ended up inside.\
\
To those people in the huts and villages of half the globe struggling to\
break the bonds of mass misery, we pledge our best efforts to help them help\
themselves, for whatever period is required -- not because the communists may\
be doing it, not because we seek their votes, but because it is right. If a\
free society cannot help the many who are poor, it cannot save the few who\
are rich.\
\
To our sister republics south of our border, we offer a special pledge -- to\
convert our good words into good deeds -- in a new alliance for progress --\
to assist free men and free governments in casting off the chains of poverty.\
But this peaceful revolution of hope cannot become the prey of hostile powers.\
Let all our neighbors know that we shall join with them to oppose aggression\
or subversion anywhere in the Americas. And let every other power know that\
this Hemisphere intends to remain the master of its own house."

pprint.pprint(getProfile(text))