import sys
import csv
import json

csvfile = open('GVP_Volcano_List.csv', 'r')
jsonfile = open('GVP_Volcano_List.json', 'w')

reader = csv.reader(csvfile, delimiter=',')
next(reader)				# Skip file header
next(reader)				# Skip csv header

jsonfile.write('[')			# Write bracket for start of list

# Assume at least one row, strip out non utf-8 chars	
row = [unicode(column, errors='ignore') for column in next(reader)]

while True:
	volcano = {}

	volcano['Volcano Number'] = row[0]
	volcano['Volcano Name'] = row[1]
	volcano['Country'] = row[2]
	volcano['Primary Volcano Type'] = row[3]
	volcano['Activity Evidence'] = row[4]
	volcano['Last Known Eruption'] = row[5]
	volcano['Region'] = row[6]
	volcano['Subregion'] = row[7]
	volcano['Latitude'] = row[8]
	volcano['Longitude'] = row[9]
	volcano['Elevation'] = row[10]
	volcano['Dominant Rock Type'] = row[11]
	volcano['Tetonic Setting'] =row[12]

	json.dump(volcano, jsonfile)

	try:
		row = [unicode(column, errors='ignore') for column in next(reader)]
	except StopIteration:
		print "Conversion Finished"
		break

	jsonfile.write(',\n')	# commas between birdstrike objects

jsonfile.write(']')			# Write bracket for end of list