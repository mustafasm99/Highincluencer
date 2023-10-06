from apscheduler.schedulers.background import BackgroundScheduler
from .function import saveOld , masterT
from datetime import datetime,timedelta
from datetime import date
import pytz

#
# background apscheduler to auto task the data save 
#

x = datetime.combine(date.today(),datetime.min.time())
current_time = datetime.now()
def start():
    s = BackgroundScheduler({'apscheduler.timezone': 'UTC'})

    s.add_job(saveOld,'interval',minutes=1440) # after on day of the time run | save the old data
    s.add_job(masterT,'interval',minutes=1440) # to save the old data to the master table | history table 
    s.start()