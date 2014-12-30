from twitter import *

t = Twitter(
    auth=OAuth('token', 'token_key', 'con_secret', 'con_secret_key'))

text = ['Essen nicht vergessen', 'Und? Mittagessen geplant?',
        'Geht jemand mit?', 'Was gibt es heute?', 'Langsam ist es Zeit.',
        'Was ist nun?', 'An Essen gedacht?', 'Wann gibt es etwas zu essen?',
        'Ihr dürft nicht vergessen zu essen.', 'Etwas essen wäre jetzt gut.',
        'Service für die üblichen Verdächtigen: schon geklärt, was es zum Mittag gibt?',
        'Etwas Essbares dabei?', 'An die üblichen Verdächtigen: Mittagessen geplant?',
        'Mittag.', 'Gegessen?', 'Dran gedacht?','Was nun?', 'Wie sieht es aus?', 'Mittag?',
        'Essen - wer noch nicht hat.', 'Schon gegessen?', 'Mittagessen gesichert?',
        'Und wer der üblichen Verdächtigen wird heute vergessen zu essen?',
        'Schon über Mittagessen nachgedacht?',
        'Service für die üblichen Verdächtigen: schon geklärt, was es zu essen gibt?']
from random import choice
random_index = choice(text)
print(random_index)
random_index2 = random_index

t.statuses.update(status = random_index2)