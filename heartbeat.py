import mraa, time, sys, atexit, signal
import pyupm_groveehr as pyupm

# heartBeat = mraa.Gpio(0)
# heartBeat.dir(mraa.DIR_)

heartBeat = pyupm.GroveEHR(0)

def SIGNINHandler(signum, frame):
    raise SystemExit

def exitCounting():
    heartBeat.stopBeatCounter()
    print "Exiting"
    sys.exit(0)

atexit.register(exitCounting)
signal.signal(signal.SIGINT, SIGNINHandler)

heartBeat.clearBeatCounter()
heartBeat.initClock()
heartBeat.startBeatCounter()

while(1):
    millis = heartBeat.getMillis()
    beats = heartBeat.beatCounter()

    fr = heartBeat.heartRate()

    outputStr = "Millis: {0} Beats: {1} Heart Beat: {2}".format(millis,beats,fr)
    print outputStr
    time.sleep(1)


