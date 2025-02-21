from datetime import datetime, timedelta
today=datetime.now()
new_d=today.replace(microsecond=0)
print(new_d)