import converters

prog = converters.Uppercase(open('spam.txt'), open('spamup.txt', 'w'))
prog.process()
