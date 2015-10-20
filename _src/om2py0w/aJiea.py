print "What's your name?" # basic info
name = raw_input()
print "Hi, %r!" % name
print " When were you born? (example: yyyy-mm-dd) "
bday = raw_input()
import datetime # generate today's date
today = datetime.date.today()

if bday == str(today) # match test
    print "Happy birthday, %!" % name
else bday != today
    print "Have a nice day,%!" % name
