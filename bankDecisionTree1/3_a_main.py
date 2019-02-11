from bankDecisionTree1 import parse_data, ID3, checkAccuracy
from anytree import Node

attributes_list = ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day",
                   "month", "duration", "campaign", "pdays", "previous", "poutcome"]

alo_type = "entropy"
alo_type1 = "majorityError"
alo_type2 = 'gini'



def main():
    # train_data, test_data, train_label, test_label = parse_data()
    # print train_data

    print "entropy--------------------------------"
    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 1, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 1 using entropy has train error:"
    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 1, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 1 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 2, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 2 using entropy has train error:"
    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 2, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 2 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 3, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 3 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 3, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 3 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 4, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 4 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 4, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 4 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 5, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 5 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 5, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 5 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 6, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 6 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 6, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 6 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 7, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 7 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 7, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 7 using entropy has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 8, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 8 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 8, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 8 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 9, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 9 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 9, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 9 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 10, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 10 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 10, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 10 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 11, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 11 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 11, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 11 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 12, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 12 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 12, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 12 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 13, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 13 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 13, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 13 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 14, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 14 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 14, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 14 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 15, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 15 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 15, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 15 using entropy has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 16, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 16 using entropy has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type, root, 16, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 16 using entropy has test error:"

    print test_error

    print "----------------------------------------------------------------------------"






    print "majority error"
    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 1, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 1 using majority error has train error:"
    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 1, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 1 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 2, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 2 using majority error has train error:"
    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 2, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 2 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 3, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 3 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 3, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 3 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 4, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 4 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 4, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 4 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 5, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 5 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 5, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 5 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 6, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 6 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 6, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 6 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 7, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 7 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 7, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 7 using majority error has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 8, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 8 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 8, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 8 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 9, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 9 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 9, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 9 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 10, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 10 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 10, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 10 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 11, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 11 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 11, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 11 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 12, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 12 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 12, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 12 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 13, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 13 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 13, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 13 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 14, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 14 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 14, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 14 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 15, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 15 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 15, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 15 using majority error has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 16, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 16 using majority error has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type1, root, 16, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 16 using majority error has test error:"

    print test_error
    print "-------------------------------------------------------------------------"

    print "gini"
    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 1, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 1 using gini has train error:"
    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 1, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 1 using gini has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 2, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 2 using gini has train error:"
    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 2, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 2 using gini has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 3, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 3 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 3, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 3 using gini has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 4, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 4 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 4, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 4 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 5, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 5 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 5, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 5 using gini has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 6, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 6 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 6, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 6 using gini has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 7, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 7 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 7, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 7 using gini has test error:"

    print test_error
    print "-----------------"


    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 8, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 8 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 8, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 8 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 9, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 9 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 9, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 9 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 10, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 10 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 10, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 10 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 11, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 11 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 11, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 11 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 12, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 12 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 12, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 12 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 13, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 13 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 13, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 13 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 14, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 14 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 14, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 14 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 15, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 15 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 15, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 15 using gini has test error:"

    print test_error
    print "-----------------"

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 16, 1)
    train_error = checkAccuracy(root, train_data, attributes_list, train_label)
    print "The decision tree with depth 16 using gini has train error:"

    print train_error

    train_data, test_data, train_label, test_label = parse_data()
    root = Node("root")
    ID3(train_data, attributes_list, train_label, alo_type2, root, 16, 1)
    test_error = checkAccuracy(root, test_data, attributes_list, test_label)
    print "The decision tree with depth 16 using gini has test error:"

    print test_error

    print "----------------------------------------------------------------------"


if __name__ == "__main__":
    main()