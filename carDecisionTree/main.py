from carDecisionTree import parse_data, ID3, checkAccuracy
from anytree import Node

attributes_list = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]
# alo_type = ["entropy", "majorityError", "gini"]

alo_type = "entropy"
alo_type1 = "majorityError"
alo_type2 = 'gini'



def main():
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
    print "-----------------------------------------------------------"






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
    print "----------------------------------------------------"

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



if __name__ == "__main__":
    main()