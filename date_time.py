from datetime import datetime

def show_time():
    now = datetime.today()

    print(now.time())
    print(now.date())

show_time()