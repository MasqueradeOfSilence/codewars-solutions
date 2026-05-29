def partition(arr, classifier_method):
    return [x for x in arr if classifier_method(x) is True], [y for y in arr if classifier_method(y) is False]