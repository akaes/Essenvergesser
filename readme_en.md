#EXPLANATION - Update: The Twitter-API has changed and the script needs an update

###TEST ENVIRONMENT: 
Mac OS X, Python 3.4

##TASK: 
Reminder to some people, which daily forget to go to lunch

##REALISATION:
Python-script sends daily at 12:00 a short-message (tweet) with different text via Twitter-API.

##REQUIREMENTS:
* a functional twitter-account

##PROCEDURE:
* registration to use the twitter-API
* generation of the needed keys for OAuth and registration
* create a list of contents for the tweets
* modification of the python-script
* setup of a cronJob (e.g. Mac OS X: xml-plist launchd) on a server

##FILES:
* essenvergesser.py - python-script for automatically tweeting
* beispiel.plist - XML-file (example) launchd (path: /Library/LaunchDaemons/)

##Docs APIs and libraries:
* [twitter-API](https://dev.twitter.com)
* [python-Library twitter](https://pypi.python.org/pypi/twitter/1.15.0)


