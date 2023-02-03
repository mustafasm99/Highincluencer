from apscheduler.schedulers.background import BackgroundScheduler
from .function import saveOld , masterT
from datetime import datetime,timedelta
from datetime import date
import pytz


x = datetime.combine(date.today(),datetime.min.time())
current_time = datetime.now()

print(x,"--",current_time)
print(current_time , current_time+timedelta(minutes=1))
def start():
    s = BackgroundScheduler({'apscheduler.timezone': 'UTC'})

    s.add_job(saveOld,'interval',minutes=1440)
    s.add_job(masterT,'interval',minutes=1440)
    s.start()