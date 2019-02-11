import csv
import os
import numpy as np

from anytree import Node

ATTRS = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
OUT_LABELS = ['unacc', 'acc', 'good', 'vgood']
NUM_OUT_LABELS = 4
BUY_MAINT_LABELS = ['vhigh', 'high', 'med', 'low']
DOORS_LABELS = ['2', '3', '4', '5more']
PERSONS_LABELS = ['2', '4', 'more']
LUG_LABELS = ['small', 'med', 'big']
SAFETY_LABELS = ['low', 'med', 'high']


# Get attribute values
def getAttrsLabels(val):
    if val == 'buying' or val == 'maint':
        return BUY_MAINT_LABELS
    elif val == 'doors':
        return DOORS_LABELS
    elif val == 'persons':
        return PERSONS_LABELS
    elif val == 'lug_boot':
        return LUG_LABELS
    elif val == 'safety':
        return SAFETY_LABELS


# Get attribute name
def getAttrsType(index):
    if index >= len(ATTRS):
        return -1

    return ATTRS[index]


# Read in data
def parseCSV(filename):
    with open(filename) as csvfile:
        temp = csv.reader(csvfile, delimiter=' ', quotechar='|')
        attrs = []
        labels = []

        for r in temp:
            currAttrs, currLabel = extractText(r[0])

            attrs.append(currAttrs)
            labels.append(currLabel)

    return attrs, labels


# Extract each row of csv file into attributes and label
def extractText(line):
    attrs = []
    numAttrs = len(ATTRS)
    itr = 0
    i = 0

    temp = ''
    while itr < numAttrs:
        if line[i] == ',':
            attrs.append(temp)
            itr += 1
            temp = ''
        else:
            temp += line[i]

        i += 1

    label = line[i:]

    return attrs, label


# Check if a given label list has the same value
def isSameLabels(labels):
    l = labels[0]
    for i in range(len(OUT_LABELS)):
        li = [x for x in labels if x != OUT_LABELS[i]]
        if len(li) > 0 and len(li) != len(labels):
            return False

    return True


# return the label with majority population
def getMajLabels(labels):
    maxNumLabel = 0;
    outLabel = labels[0]
    for i in range(len(OUT_LABELS)):
        li = [x for x in labels if x == OUT_LABELS[i]]
        if len(li) > maxNumLabel:
            maxNumLabel = len(li)
            outLabel = OUT_LABELS[i]
    return outLabel


# decision tree construction
def ID3(data, labels, attrsList, depth, algoType):
    if isSameLabels(labels) or depth < 1:
        return getMajLabels(labels)

    else:
        # Pick attribute using information gain
        root = findMaxInfoAttrs(data, labels, attrsList, algoType)

        val_root = getAttrsLabels(root)
        val_root_index = attrsList.index(root)

        newAttrsList = attrsList[:val_root_index]
        if val_root_index == len(ATTRS) - 1:
            new_data = [v[:-1] for v in data]
        else:
            new_data = [v[:val_root_index] + v[val_root_index + 1:] for v in data]
            newAttrsList += attrsList[val_root_index + 1:]

        val = []
        for i in range(len(val_root)):
            sub_labels = [v for v, x in zip(labels, data) if x[val_root_index] == val_root[i]]
            sub_data = [v for v, x in zip(new_data, data) if x[val_root_index] == val_root[i]]

            # If attribute is missing, return the most common label
            if len(sub_data) == 0:
                val.append(getMajLabels(labels))
            else:
                # Recursively build sub-tree
                val.append(ID3(sub_data, sub_labels, newAttrsList, depth - 1, algoType))
        return {root: val}


# Find attribute with max information gain
def findMaxInfoAttrs(attrs, labels, attrs_labelsList, algoType='entropy'):
    h_total = computeImpurity(labels, OUT_LABELS, algoType)

    numAttrsL = len(attrs_labelsList)
    infoVec = np.zeros((numAttrsL, 1))
    for i in range(numAttrsL):
        currAttrs = [attrs[x][i] for x in range(len(attrs))]

        currInfo = computeInfoGain(currAttrs, labels, attrs_labelsList[i], h_total, algoType)
        infoVec[i] = currInfo
        val = attrs_labelsList[np.argmax(infoVec)]

    return val


# Compute information gain
def computeInfoGain(attrs, labels, attrs_label, h_total, cat='entropy'):
    labelsList = getAttrsLabels(attrs_label)
    expect_entropy = 0.0

    for i in range(len(labelsList)):
        tempVal = [v for v, x in zip(labels, attrs) if x == labelsList[i]]

        if len(tempVal) > 0:
            currE = computeImpurity(tempVal, OUT_LABELS, cat)
        else:
            currE = 0.0

        expect_entropy += currE * (len(tempVal) / len(attrs))

    infoG = h_total - expect_entropy

    return infoG


# Compute impurity metric
def computeImpurity(data, labels, cat='entropy'):
    numLabels = len(labels)
    numTotal = len(data)

    impurity = 0.0;
    maxImpurity = -1.0
    for i in range(numLabels):
        currN = data.count(labels[i])

        # Using entropy
        if cat == 'entropy':
            if currN != 0.0:
                impurity += (-currN / numTotal) * np.log2(currN / numTotal)
        # Using majority error
        elif cat == 'majority':
            maj_error = currN / numTotal
            if maj_error > maxImpurity:
                maxImpurity = maj_error
                impurity = maj_error

    return impurity


# Calculate accuracy of prediction
def accuracy(predict, label):
    accr = 0.0
    for pVal, lVal in zip(predict, label):
        if pVal == lVal:
            accr += 1

    return accr / len(label)


# Use decision tree to predict an event
def predict(inp, tree):
    a = [x for x in tree][0]
    newDict = tree[a]
    while len(a) > 0:
        currL = getAttrsLabels(a)

        val = newDict[currL.index(inp[ATTRS.index(a)])]

        a = [x for x in val][0]

        if a not in ATTRS:
            return val
        else:
            newDict = val[a]


def Main():
    testAttrs, testLabels = parseCSV(os.getcwd() + '/test.csv')
    trainAttrs, trainLabels = parseCSV(os.getcwd() + '/train.csv')
    print trainAttrs
    print trainLabels
    algoType = ['entropy', 'majority']
    for k in range(len(algoType)):
        for i in range(1, 8):
            currTree = ID3(trainAttrs, trainLabels, ATTRS, i, algoType[k])

            # Get test error
            currTestPred = [predict(x, currTree) for x in testAttrs]
            currTestAccr = accuracy(currTestPred, testLabels)

            # Get train error
            currTrainPred = [predict(x, currTree) for x in trainAttrs]
            currTrainAccr = accuracy(currTrainPred, trainLabels)

            print('Decision Tree of depth %s using ' % i + algoType[k] + ': Test Error = %.6f; Train Error = %.6f'
                  % (currTestAccr, currTrainAccr))


Main()




# buying_vhigh = 0
# buying_vhigh_unacc = 0
# buying_vhigh_acc = 0
# buying_vhigh_good = 0
# buying_vhigh_vgood = 0
#
# buying_high = 0
# buying_high_unacc = 0
# buying_high_acc = 0
# buying_high_good = 0
# buying_high_vgood = 0
#
# buying_med = 0
# buying_med_unacc = 0
# buying_med_acc = 0
# buying_med_good = 0
# buying_med_vgood = 0
#
# buying_low = 0
# buying_low_unacc = 0
# buying_low_acc = 0
# buying_low_good = 0
# buying_low_vgood = 0
#
# maint_vhigh = 0
# maint_vhigh_unacc = 0
# maint_vhigh_acc = 0
# maint_vhigh_good = 0
# maint_vhigh_vgood = 0
#
# maint_high = 0
# maint_high_unacc = 0
# maint_high_acc = 0
# maint_high_good = 0
# maint_high_vgood = 0
#
# maint_med = 0
# maint_med_unacc = 0
# maint_med_acc = 0
# maint_med_good = 0
# maint_med_vgood = 0
#
# maint_low = 0
# maint_low_unacc = 0
# maint_low_acc = 0
# maint_low_good = 0
# maint_low_vgood = 0


# class Node:
#     value = ""
#     children = []
#
#     def __init__(self, val, dictionary):
#         self.set_value(val)
#         self.gen_children(dictionary)
#
#     def set_value(self, val):
#         self.value = val
#
#     def gen_children(self, dictionary):
#         if isinstance(dictionary, dict):
#             self.children = dictionary.keys()


# CST_attributes = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
# CST_buying = ['vhigh', 'high', 'med', 'low']
# CST_maint = ['vhigh', 'high', 'med', 'low']
# CST_doors = ['2', '3', '4', '5more']
# CST_persons = ['2', '4', 'more']
# CST_lug_boot = ['small', 'med', 'big']
# CST_safety = ['low', 'med', 'high']
# CST_attributes_dict = {'buying': CST_buying, 'maint': CST_maint, 'doors': CST_doors, 'persons': CST_persons,
#                        'lug_boot': CST_lug_boot, 'safety': CST_safety}
# att_list = []