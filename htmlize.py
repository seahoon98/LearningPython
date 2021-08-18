from converters import Uppercase

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line[:-1])

Uppercase(open('spam.txt'), HTMLize()).process()
