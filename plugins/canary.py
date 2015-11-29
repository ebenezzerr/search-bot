import time
outputs = []

def canary():
    #NOTE: you must add a real channel ID for this to work
    outputs.append(["D0FEYBP9V", "bot started: " + str(time.time())])

canary()
