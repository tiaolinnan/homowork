import csv
import pandas as pd
import numpy as numpy
import collections as collections
import math
from itertools import compress
from anytree import Node,RenderTree


algoType = ["entropy", "majorityError", "gini"]
depth_limit = 5

answer = 0.0

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = {}
#
#     def append(self, feature, data):
#         self.children[feature] = data
#

def parse_data():

    train_file = pd.read_csv('train.csv', sep=',', header=None)
    test_file = pd.read_csv('test.csv', sep=',', header=None)

    train_data = train_file.iloc[:, 0:len(train_file.columns) - 1].values
    test_data = test_file.iloc[:, 0:len(test_file.columns) - 1].values

    train_label = train_file.iloc[:, len(train_file.columns) - 1].tolist()
    test_label = test_file.iloc[:, len(test_file.columns) - 1].tolist()

    return train_data, test_data, train_label, test_label


def ID3(S, attributes, labels, aloType, tree_root, max_dep, depth):
    if len(set(labels)) == 1:
        Node("leaf=" + labels[0], parent= tree_root)
        return labels[0]

    elif len(attributes) == 0 or depth > max_dep:
        # check the most common value
        leaf = max(set(labels), key=labels.count)
        Node("leaf=" + leaf, parent = tree_root)
        return leaf
    # otherwise
    else:
        # compute which attribute best split S
        basePurity = computeBasePurity(labels, aloType)
        # print "basePurty: " + str(basePurity)
        best_attribute = computeBstSplit_S(S, labels, basePurity, aloType)
        # print best_attribute
        attr_node = Node(attributes[best_attribute], parent= tree_root)
        # for each possible value of A
        for attr in set(S[:, best_attribute].tolist()):
            # attr value is the new node, parent is the attr name
            attr_value_node = Node(attr, parent=attr_node)
            # print "attr: " + str(attr)
            Sv = S[S[:, best_attribute] == attr]
            # print "Sv: " + str(Sv)
            # print len(Sv)

            if Sv.size == 0:
                mostCommonLabel = max(set(labels), key=labels.count)
                Node("leaf="+mostCommonLabel, parent=attr_value_node)
            else:
                # delete from y axis
                Sv = numpy.delete(Sv, best_attribute, 1)
                # print "Sv change:" + str(Sv)
                # print len(Sv)
                filter = (S[:,best_attribute] == attr).tolist()
                # print "filter" + str(filter)
                #get the new label list base on the best attribute
                newLabel = list(compress(labels, filter))
                # newAttributes = attributes.remove(attributes[best_attribute])
                # print type(attributes)
                # print type(newAttributes)
                newAttributes = attributes[:]
                newAttributes.remove(attributes[best_attribute])
                ID3(Sv, newAttributes, newLabel, aloType, attr_value_node, max_dep, depth + 1)
    # print "tree" + str(tree_root)
    return tree_root

def computeBstSplit_S(S, labels, basePur, alotype):
    column_number = S.shape[1]
    best_column = -1
    best_ig = float("inf")
    for clm in xrange(column_number):
        # print "clm : " + str(clm)
        current_column_exppurity = expectedPurity(S[:, clm].tolist(), labels, alotype)
        current_ig = basePur - current_column_exppurity
        if best_ig > current_ig:
            best_ig = current_ig
            best_column = clm
    return best_column


def expectedPurity(S_list, labels, alotype):
    # print set(S_list)
    result = 0.0
    S_list = numpy.array(S_list)
    count = collections.Counter(S_list)
    for item in set(S_list):
        ratio = count[item]/float(len(S_list))
        element = [labels[i] for i in xrange(len(S_list)) if S_list[i] == item]
        # print "list: " + str(element)
        result = result + ratio * computeBasePurity(element, alotype)
    return result


def computeBasePurity(labels, aloType):
    # count each # of item in one collumn
    labels_list = numpy.array(labels)
    count = collections.Counter(labels_list)

    result = 0.0
    summation = 0.0

    for item in set(labels):
        # print count[item]
        # print len(labels)
        ratio = count[item]/float(len(labels))

        # print "ratio: " + str(rationumber)
        if aloType == "entropy":
            # print "entro:"
            result -= ratio * math.log(ratio, 2)

        elif aloType == "majorityError":
            # print "maj"
            if ratio > result:
                result = ratio

        else:
            # print "else"
            summation += math.pow(ratio, 2)

            gini = 1 - summation
            result = gini
    return result


def predict(tree_root, data, attributes):
    if tree_root.name.startswith("leaf="):
        return tree_root.name[2:]
    else:
        node_name = tree_root.name
        data_index = attributes.index(node_name)
        data_value = data[data_index]
        for kid in tree_root.children:
            if kid.name == data_value:
                return predict(kid.children[0], data, attributes)


def checkAccuracy(tree_root, data, attributes, labels):
    tree_root = tree_root.children[0]
    row_len = data.shape[0]
    error_count = 0
    for x in xrange(row_len):
        ans = predict(tree_root, data[x, :], attributes)
        # print ans[3:]
        # print labels[x]
        # print ans

        if ans == None or ans[3:] != labels[x]:
            error_count = error_count + 1
    # print error_count
    # '%.2f' % (a / b)
    ratio = '%.6f' % (error_count/float(row_len))
    return ratio
    # return error_count/float(row_len)


# def main():
#     train_data, test_data, train_label, test_label = parse_data()
#     root = Node("root")
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 3, 1)
#     answer = checkAccuracy(root, train_data, attributes_list, train_label)
#     print answer
#
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 2, 1)
#     answer = checkAccuracy(root, train_data, attributes_list, train_label)
#     print answer
#
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 3, 1)
#     answer = checkAccuracy(root, train_data, attributes_list, train_label)
#     print answer
#
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 4, 1)
#     answer = checkAccuracy(root, train_data, attributes_list, train_label)
#     print answer
#
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 5, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 6, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'majorityError', root, 7, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 1, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 2, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 3, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 4, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 5, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 6, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio
#
#     root = ID3(train_data, attributes_list, train_label, 'entropy', root, 7, 1)
#     ratio = checkAccuracy(root, train_data, attributes_list, train_label)
#     print ratio


    # for x in xrange(len(algoType)):
    # for dep in xrange(1,8):
    # print dep
    # root = ID3(train_data, attributes_list, train_label, "entropy", root, 1, 1)
    # accurrcy = checkAccuracy(root, train_data, attributes_list, train_label)
    # print accurrcy
    #
    # root = ID3(train_data, attributes_list, train_label, "entropy", root, 2, 1)
    # accurrcy = checkAccuracy(root, train_data, attributes_list, train_label)
    # print accurrcy
        # print dep
        # print accurrcy


    # ratio = checkAccuracy(root, train_data, attributes_list, train_label)
    # print ratio


    # for pre, fill, node in RenderTree(root):
    #     print("%s%s" % (pre, node.name))

    # testAttrs, testLabels = parseCSV(os.getcwd() + '/test.csv')
    # trainAttrs, trainLabels = parseCSV(os.getcwd() + '/train.csv')
    # print trainAttrs
    # print trainLabels
    # algoType = ['entropy', 'majority']
    # for k in range(len(algoType)):
    #     for i in range(1, 8):
    #
    #         currTree = ID3(trainAttrs, trainLabels, ATTRS, i, algoType[k])
    #
    #         # Get test error
    #         currTestPred = [predict(x, currTree) for x in testAttrs]
    #         currTestAccr = accuracy(currTestPred, testLabels)
    #
    #         # Get train error
    #         currTrainPred = [predict(x, currTree) for x in trainAttrs]
    #         currTrainAccr = accuracy(currTrainPred, trainLabels)
    #
    #         print('Decision Tree of depth %s using ' % i + algoType[k] + ': Test Error = %.6f; Train Error = %.6f'
    #               % (currTestAccr, currTrainAccr))





# if __name__ == "__main__":
#     main()