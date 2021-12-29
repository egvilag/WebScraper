import csv

csv_file_names = ['cpu_intel.csv', 'cpu_amd.csv']
final_csv_headers = ['company', 'family', 'model', 'platform', 'lithography', 'socket', '# of cpu cores', '# of threads', 'launch date', 'l3 cache', 'l2 cache', 'unlocked', 'base clock', 'tdp', 'max boost clock', 'memory type', 'maximum memory speed', 'pci-e support', 'max cpu configuration', '# of memory channels', 'cooler']
temp_csv = []
final_csv = []
final_csv_column = 0
csv_content = []

#read csv file
#putting csv contents into one 2d list: csv_content[n]
#where n is the nth csv content
for file in csv_file_names:
    csv_data = []
    with open(file, 'r') as csv_file:
        print('opening the csv file')
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_data.append(row)
    csv_content.append(csv_data)

#checking list length
file_count = 0
for file in csv_content:
    print(len(file[0]))
    for line in file:
        while len(file[0]) > len(line):
            line.append('')
            #print('Rövidebb')
        #print(len(line))
    file_count += 1

#add predefinied headers to the final csv list
headers = []
headers.append(final_csv_headers)
temp_csv.append(headers)

#create 2d array
rows = []
temp_list = []

#cycle through the columns
for file in csv_content:
    final_csv_column = 0

    #new entries to write in
    for row, csv_data_rows in enumerate(file):
        temp_list = []
        for i in range(len(final_csv_headers)):
            temp_list.append('')
        rows.append(temp_list)

    for column in range(len(file[0])):
         #if column's first cell's value equals to
        if file[0][column] == 'Product Collection' or file[0][column] == 'Family':
            final_csv_column = 1
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]
            
        #if column's first cell's value equals to
        if file[0][column] == 'Processor Number' or file[0][column] == 'Model':
            final_csv_column = 2
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Vertical Segment' or file[0][column] == 'Platform':
            final_csv_column = 3
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Lithography' or file[0][column] == 'Processor Technology for CPU Core':
            final_csv_column = 4
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]
            
        #if column's first cell's value equals to
        if file[0][column] == 'Sockets Supported' or file[0][column] == 'CPU Socket':
            final_csv_column = 5
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == '# of CPU Cores' or file[0][column] == 'Total Cores':
            final_csv_column = 6
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == '# of Threads' or file[0][column] == 'Total Threads':
            final_csv_column = 7
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Launch Date':
            final_csv_column = 8
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Total L3 Cache' or file[0][column] == 'Cache':
            final_csv_column = 9
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Total L2 Cache':
            final_csv_column = 10
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Unlocked for Overclocking':
            final_csv_column = 11
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Base Clock' or file[0][column] == 'Processor Base Frequency':
            final_csv_column = 12
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Default TDP' or file[0][column] == 'TDP':
            final_csv_column = 13
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Max. Boost Clock 1 2' or file[0][column] == 'Max Turbo Frequency':
            final_csv_column = 14
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'System Memory Type' or file[0][column] == 'Memory Types':
            final_csv_column = 15
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'System Memory Specification' or file[0][column] == 'Maximum Memory Speed':
            final_csv_column = 16
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'PCI Express® Version' or file[0][column] == 'PCI Support':
            final_csv_column = 17
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Socket Count' or file[0][column] == 'Max CPU Configuration':
            final_csv_column = 18
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Memory Channels' or file[0][column] == 'Max # of Memory Channels':
            final_csv_column = 19
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]

        #if column's first cell's value equals to
        if file[0][column] == 'Thermal Solution PIB':
            final_csv_column = 20
            #loop through every row
            for row, csv_data_rows in enumerate(file):
                if row != 0:
                    rows[row-1][final_csv_column] = file[row][column]
                    
    temp_csv.append(rows)
    rows = []

#print the whole 2d list
#for i in range(len(temp_csv)):
#    for j in range(len(temp_csv[i])):
#        print(temp_csv[i][j])

#print('writing csv')

with open('cpu.csv', 'w', newline = '') as csv_file:
     write = csv.writer(csv_file)
     for i in range(len(temp_csv)):
        for j in range(len(temp_csv[i])):
            if temp_csv[i][j][1] != '':
                write.writerow(temp_csv[i][j])

print('done')
