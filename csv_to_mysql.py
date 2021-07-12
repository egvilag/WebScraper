import mysql.connector
import csv

csv_file_name = ''
db_ip = ''
db_user = ''
db_user_pw = ''
db_name = ''
db_tbl_name = ''

# read the CSV file line by line
# first line is the header
# put the lines into lists
data = []
line_count = 0
with open(csv_file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                data.append(row)

# connect to db with the provided info
db = mysql.connector.connect(
    host=db_ip,
    user=db_user,
    password=db_user_pw,
    database=db_name
)

# define db cursor with the needed attributes
db_cursor = db.cursor(dictionary=True, buffered=True)

# uncomment these to create the database and the table
#db_cursor.execute("CREATE DATABASE IF NOT EXISTS webshop")
#db_cursor.execute("DROP TABLE IF EXISTS cpu_amd")
#db_cursor.execute("CREATE TABLE IF NOT EXISTS cpu_amd (id INT AUTO_INCREMENT PRIMARY KEY)")

# uncomment these to set the headers in db table
# for i in range(len(header)):
#    column_name = header[i]
#    query = "ALTER TABLE cpu_amd ADD `{}` TEXT".format(column_name)
#    db_cursor.execute(query)

# processing the lists
for i in range(len(data)):
    column_name = header[0]
    value = data[i][0]
    query = "SELECT * FROM {} WHERE `{}` = '{}'".format(
        db_tbl_name, header[0], value)
    db_cursor.execute(query)
    db.commit()
    found = 0
    j = 0
    # if there is something in db_cursor variable
    # commit the update
    for row in db_cursor:
        found = "1"
        if found == "1":
            for row in (header):
                query = "UPDATE {} SET `{}` = '{}' WHERE `{}` = '{}'".format(
                    db_tbl_name, header[j], data[i][j], header[0], value)
                j += 1
                db_cursor.execute(query)
                # db.commit()
    # if there isn't anything in db_cursor variable
    # commit the first element from the variable
    if found == 0:
        query = "INSERT INTO {} (`{}`) VALUES ('{}')".format(
            db_tbl_name, header[0], data[i][0])
        db_cursor.execute(query)
        db.commit()
        for row in (header):
            query = "UPDATE '{}' SET `{}` = '{}' WHERE `{}` = '{}'".format(
                db_tbl_name, header[j], data[i][j], header[0], value)
            j += 1
            db_cursor.execute(query)
    db.commit()
