#!/usr/bin/env python
import datetime
import TheHitList
import csv

thl = TheHitList.Application()

# Datetime -> Number
def getDays(date):
	return getOffset((date - datetime.date.today()).days)

def getOffset(n):
	if n == 0:
		return "Today"
	elif n == 1:
		return "Tomorrow"
	elif n == -1:
		return "Yesterday"

	posn = abs(n)
	days = posn%7
	if posn > 11000:
		return ""
	weeks = (posn-days)/7

	datestring = ""
	if weeks == 1:
		datestring += "1 week"
	elif weeks:
		datestring += "%d weeks" % weeks	
	if days == 1:
		datestring += "1 day"
	elif days:
		datestring += "%d days" % days

	if posn != n:
		datestring += " ago"
	else:
		datestring = "In " + datestring
	return datestring


def makelist():
	tasks = []
	for task in thl.today().tasks():
		if not task.completed or task.canceled:
			if(task.due_date is not None):
				tasks.append([task.title, task.due_date.date()])
			else:
				tasks.append([task.title, datetime.date.fromtimestamp(100000000000)])
	sorted_by_second = sorted(tasks, key=lambda tup: tup[1])
	return map(getrealdate, sorted_by_second)

def getrealdate(task):
	return [task[0], getDays(task[1])]

with open('/Volumes/Voskhod/Dropbox/thlstuff/thl.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',
							quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(["75%", "25%"])                        
	for task in makelist():
		writer.writerow(task)

#	for task in thl.today().tasks():
#		writer.writerow(makelist(task))
