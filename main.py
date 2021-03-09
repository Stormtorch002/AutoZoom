import webbrowser
import csv
import time
import datetime


def get_dt_obj(row):
	t = row[1]
	t = t.split(':')
	h, m = int(t[0]), int(t[1])
	t_obj = datetime.datetime.now()
	return t_obj.replace(hour=h, minute=m, second=0)


with open('./schedule.csv') as f:
	reader = csv.reader(f, delimiter=',')

	for row in reader:
		try:
			name = row[2]
		except IndexError:
			name = ''
			
		link = row[0]

		t_obj = get_dt_obj(row)
		now = datetime.datetime.now()

		if t_obj < now:
			continue

		delta = (t_obj - now).total_seconds()

		print(f'Opening {name} at {row[1]}')
		time.sleep(delta)
		print(f'Opening {name}...')
		webbrowser.open(link)
