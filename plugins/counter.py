import time
crontable = []
outputs = []

crontable.append([120,"say_time"])

def say_time():
    #NOTE: you must add a real channel ID for this to work
    outputs.append(["D0FEYBP9V", time.time()])
