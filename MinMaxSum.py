# function that determines the minimum sum of 4 of 5 integers and the maximum sum 

def miniMaxSum(intList):
    print(sum(intList) - max(intList),sum(intList) - min(intList))
inputList = input("List 5 integers with spaces in between them: ").split()
miniMaxSum(list(map(int, inputList)))
