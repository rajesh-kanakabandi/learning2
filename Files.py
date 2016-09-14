"""
    Files.py
    introduction to File I/O:
    open - to open a file.
    file object has a an iterator which gives a list of line objects

Assignment:
    write a program to print fibonacii series(first 30) to a file.
    * 10 items per line.
    * seperated by ', '

    0 1 1 2 3 5 8........


"""


def read_file():
    try:
        fileObj = open('data_structures.txt')
    except IOError as e:
        print(str(e))
        return
    for line in fileObj:
        print(line)
    fileObj.close()

#read_file()

def safe_read():
    with open('data_structures.txt') as fileObj:
        for line in fileObj:
            print(line)
    print("Bye")


#safe_read()

def log():
    fileObj = open('log.txt', 'a')
    fileObj.write('this is my first line1\n')
    fileObj.close()


#log()



",".join(['1', '2', '3'])


def write_csv():
    data_records = [['rajesh', 'dev', 'python'],
                    ['john', 'dev','java']]
    fp = open('dev_data.csv','w')
    for item in data_records:
        fp.write(",".join(item) + "\n")
    fp.close()

#write_csv()
def my_read_csv():
    fp = open('dev_data.csv', 'r')
    for data in fp:
        print(data.split(','))

#my_read_csv()

import csv
def read_csv():
    fp = open('dev_data.csv','r')
    data_records = csv.reader(fp, delimiter=',')
    for data in data_records:
        print(data)

#read_csv()

def write_csv():
    data_records = [['rajesh', 'dev', 'python'],
                    ['john', 'dev','java']]
    fp = open('dev_data2.csv','w')
    csv_writer = csv.writer(fp, delimiter='#')
    for item in data_records:
        csv_writer.writerow(item)
    fp.close()


write_csv()

#
#
# logging

import logging
logging.basicConfig(filename='learning.log',level=logging.NOTSET)

logging.error("I am an error")
logging.debug("I am here for debugging purposes")
logging.info("I am logging some important info for you.")
logging.critical("there is a critically wrong situation")
logging.warning("there is a warning situation")
list1 = []
j=0
