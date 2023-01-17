import csv
import mysql.connector


with mysql.connector.connect(user='sql11589833', password='XLhUkHR3ml', host='sql11.freemysqlhosting.net', database='sql11589833') as connection:
    cursor = connection.cursor()

# with open('cities.csv') as csvfile:
#     reader = csv.reader(csvfile)

#     for row in reader:
#         print(row[2])