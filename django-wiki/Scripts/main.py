from datetime import datetime, timedelta
import time
import sys
from sched import scheduler
import os
import django

sys.path.append(r'..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from Scripts.treeview_importer import addLinksToTreeView
from Scripts.bsiImporter import doUpdate, post_phase, doImport
from bsiwiki import settings

#from Scripts.bsiCrawler.main import crawlTranslateTreeview
#from Scripts.bsiWizard.topicGeneration import topicGeneration
#from Scripts.bsiComparator.bsicomparator import compare
isRunning = False

def update_phase():
    global isRunning
    isRunning = True
    now = datetime.now()
    archive_date = str(now.year) + '-' + str(now.month)
    delay = timedelta(days =30).total_seconds()

    print('Entering mid-phase on:', now)

    # call crawler + translator + treeview generation
    #crawlTranslateTreeview()

    # call topic generation for the wizard
    #topicGeneration()

    # call comparator
   # file = compare()

    # call treeview importer
    #addLinksToTreeView()


    # enter mid phase
    doUpdate(settings.COMPARATOR_OUTPUT)
    # wait 30 days and then execute post phase
    s = scheduler(time.time, time.sleep)
    s.enter(delay, 1,  post_phase(datetime.now().strftime("%Y-%m-%d") , settings.COMPARATOR_OUTPUT)
                                                       , archive_date)
    s.run()

    print('Post-phase has been executed.')
    isRunning = False


def check_update_progress():
    return isRunning

'''
def demo_mid_phase():
    # for the demo we don't call crawlers and co
    doUpdate('./../Seel-17-18/programming/bsiComparator/example_modified_files.txt')


def demo_post_phase():
    post_phase(datetime.now().strftime("%Y-%m-%d") , '/home/ziik/Seel-17-18/programming/bsiComparator/example_modified_files.txt')

'''

if __name__ == "__main__":
    doImport()
