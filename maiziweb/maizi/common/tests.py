from django.test import TestCase

# Create your tests here.

f2 =open("c.bat",'a+')

for a in xrange(10000):
    tt = 'telnet 127.0.0.1 ' + str(a) + '\n'
    f2.writelines(tt)
