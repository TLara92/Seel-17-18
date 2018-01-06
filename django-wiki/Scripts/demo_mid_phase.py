from bsiImporter import mid_phase
from sched import scheduler
import time

def midPhase():
    scheduler = scheduler(time.time, time.sleep)
    print('Entering mid-phase...')
    scheduler.enter(0, 1, mid_phase, ())
    scheduler.run()