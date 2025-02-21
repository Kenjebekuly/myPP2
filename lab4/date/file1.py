from datetime import datetime, timedelta
today=datetime.now()
new_d=today-timedelta(days=5)
print(new_d.strftime('%Y-%m-%d'))