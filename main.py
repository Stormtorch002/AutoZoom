import webbrowser
import csv
import time
import datetime


def get_dt_obj(row):
	t = row[1]
	t = t.split(':')
	h, m = int(t[0]), int(t[1])
	t_obj = datetime.datetime.now()
	return t_obj.replace(hour=h, minute=m)


with open('./schedule.csv') as f:
	reader = csv.reader(f, delimiter='\t')
	reader = list(reader).sort(key=get_dt_obj)


	for row in reader:
		t_obj = get_dt_obj(row)
		now = datetime.datetime.now()

		if t_obj < now:
			continue

		delta = (t_obj - now).total_seconds()
		time.sleep(delta)

		webbrowser.open(row[0])
