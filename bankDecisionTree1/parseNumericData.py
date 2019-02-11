import csv
import pandas as pd
from numpy import median


def parse_data():

    train_file = pd.read_csv('train.csv', sep=',', header=None)

    # print train_file
    mid0 = median(train_file[0])
    for x in xrange(len(train_file[0])):
        if train_file[0][x] > mid0:
            train_file[0][x] = 1
        else:
            train_file[0][x] = 0

    mid9 = median(train_file[5])
    for x in xrange(len(train_file[5])):
        if train_file[5][x] > mid9:
            train_file[5][x] = 1
        else:
            train_file[5][x] = 0

    mid9 = median(train_file[9])
    for x in xrange(len(train_file[9])):
        if train_file[9][x] > mid9:
            train_file[9][x] = 1
        else:
            train_file[9][x] = 0

    mid11 = median(train_file[11])
    for x in xrange(len(train_file[11])):
        if train_file[11][x] > mid11:
            train_file[11][x] = 1
        else:
            train_file[11][x] = 0

    mid12 = median(train_file[12])
    for x in xrange(len(train_file[12])):
        if train_file[12][x] > mid12:
            train_file[12][x] = 1
        else:
            train_file[12][x] = 0

    mid13 = median(train_file[13])
    for x in xrange(len(train_file[13])):
        if train_file[13][x] == -1:
            train_file[13][x] = -1
        elif train_file[13][x] > mid13:
            train_file[13][x] = 1
        else:
            train_file[13][x] = 0


    mid14 = median(train_file[14])
    for x in xrange(len(train_file[14])):
        if train_file[14][x] > mid14:
            train_file[14][x] = 1
        else:
            train_file[14][x] = 0

    test_file = pd.read_csv('test.csv', sep=',', header=None)

    # print train_file
    mid0 = median([0])
    for x in xrange(len(test_file[0])):
        if test_file[0][x] > mid0:
            test_file[0][x] = 1
        else:
            test_file[0][x] = 0

    mid9 = median(test_file[5])
    for x in xrange(len(test_file[5])):
        if test_file[5][x] > mid9:
            test_file[5][x] = 1
        else:
            test_file[5][x] = 0

    mid9 = median(test_file[9])
    for x in xrange(len(test_file[9])):
        if test_file[9][x] > mid9:
            test_file[9][x] = 1
        else:
            test_file[9][x] = 0

    mid11 = median(test_file[11])
    for x in xrange(len(test_file[11])):
        if test_file[11][x] > mid11:
            test_file[11][x] = 1
        else:
            test_file[11][x] = 0

    mid12 = median(test_file[12])
    for x in xrange(len(test_file[12])):
        if test_file[12][x] > mid12:
            test_file[12][x] = 1
        else:
            test_file[12][x] = 0

    mid13 = median(test_file[13])
    for x in xrange(len(test_file[13])):
        if test_file[13][x] == -1:
            test_file[13][x] = -1
        elif test_file[13][x] > mid13:
            test_file[13][x] = 1
        else:
            test_file[13][x] = 0

    mid14 = median(test_file[14])
    for x in xrange(len(test_file[14])):
        if test_file[14][x] > mid14:
            test_file[14][x] = 1
        else:
            test_file[14][x] = 0






    train_data = train_file.iloc[:, 0:len(test_file.columns) - 1].values

    test_data = test_file.iloc[:, 0:len(test_file.columns) - 1].values

    return train_data, test_data

if __name__ == "__main__":

    train_data, test_data = parse_data()

    with open('new_train.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerows(train_data)

    with open('new_test.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerows(test_data)