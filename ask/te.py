import os
bd = os.path.dirname(os.path.dirname(__file__))
bd = os.path.curdir

tp = os.path.join(bd, "template")

print "bd = '%s'\ntp = '%s'" % (bd, tp)
