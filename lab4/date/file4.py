from datetime import datetime, timedelta
date_format="%Y-%m-%d %H:%M:%S"
date1_str=input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str=input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date1=datetime.strptime(date1_str, date_format)
date2=datetime.strptime(date2_str, date_format)
difference_in_seconds = abs((date1-date2).total_seconds())
print("Difference between two dates in seconds:", difference_in_seconds)