import sys
def printProgress(step=0, totalSteps=0, seconds=None, barWidth=20):
    progress = float(step)/float(totalSteps)
    nHashes = int(round(barWidth*progress))
    percent = int(round(progress*100))
    if seconds is None:
        print ("[" + ("-"*nHashes) + (" "*(barWidth-nHashes)) + "] " + str(percent) + "%   \r"),
    else:
        secondsLeft = (seconds/step) * (totalSteps-step)
        m, s = divmod(secondsLeft, 60)
        h, m = divmod(m, 60)
        s = int(s)
        m = int(m)
        h = int(h)
        print ("[" + ("-"*nHashes) + (" "*(barWidth-nHashes)) + "] " + str(percent) + "%, ETA = " + str(h) + ":" + str(m) + ":" + str(s) + "   \r"),
    sys.stdout.flush()
