from datetime import datetime

date = datetime.now()
formated_date = date.strftime('%Y-%m-%d %H:%M:%S')
print(formated_date)
