def import_mt_log(file):
	from pathlib import Path
	input_path = Path(file)
	input_file = open(input_path, mode = "rt")
	input_read = input_file.read()
	input_read = input_read.split(sep="\n")
	data = list()
	for x in input_read:
		if x.find("ACTION") != -1:
			y = x.split(":")
			if y[4].find(".") == -1 and y[4].find("[") == -1 and y[4].find("MOD") == -1:
				data.append(x)
			elif y[4].find("joins game") != -1:
				data.append(x)
	f_data = dict()
	for x in data:
		year = x[:4]
		month = x[5:7]
		day = x[8:10]
		hour = x[11:13]
		minute = x[14:16]
		second = x[17:19]
		try:
			f_data[year]
		except:
			f_data[year] = dict()
		try:
			f_data[year][month]
		except:
			f_data[year][month] = dict()
		try:
			f_data[year][month][day]
		except:
			f_data[year][month][day] = dict()
		try:
			f_data[year][month][day][hour]
		except:
			f_data[year][month][day][hour] = dict()
		try:
			f_data[year][month][day][hour][minute]
		except:
			f_data[year][month][day][hour][minute] = dict()
		try:
			f_data[year][month][day][hour][minute][second]
		except:
			f_data[year][month][day][hour][minute][second] = list()
		if x[35:].find("Server:") == -1:
			f_data[year][month][day][hour][minute][second].append(x[37:])
		else:
			f_data[x[:4]][x[5:7]][x[8:10]][x[11:13]][x[14:16]][x[17:19]].append(x[35:])
	return f_data
