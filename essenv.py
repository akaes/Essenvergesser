from twitter import *

t = Twitter(
    auth=OAuth('token', 'token_key', 'con_secret', 'con_secret_key'))

text = [
    'Essen nicht vergessen','Und? Mittagessen geplant?','Geht jemand mit?',\n\
    'Was gibt es heute?','Langsam ist es Zeit.',\n\
    'Was ist nun?', 'An Essen gedacht?', 'Wann gibt es etwas zu essen?',\n\
    'Ihr dürft nicht vergessen zu essen.', 'Etwas essen wäre jetzt gut.',\n\
    'Service für die üblichen Verdächtigen: schon geklärt, was es zum Mittag gibt?',\n\
    'Etwas Essbares dabei?', 'An die üblichen Verdächtigen: Mittagessen geplant?',\n\
    'Mittag.', 'Gegessen?', 'Dran gedacht?','Was nun?', 'Wie sieht es aus?', 'Mittag?',\n\
    'Essen - wer noch nicht hat.', 'Schon gegessen?', 'Mittagessen gesichert?',\n\
    'Und wer der üblichen Verdächtigen wird heute vergessen zu essen?',\n\
    'Schon über Mittagessen nachgedacht?',\n\
    'Service für die üblichen Verdächtigen: schon geklärt, was es zu essen gibt?'\n\
    ]
from random import choice
random_index = choice(text)
print(random_index)
random_index2 = random_index

t.statuses.update(status = random_index2)
