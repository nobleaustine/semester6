
# function to take user inputs 
def get_matrix():
    no_class = int(input("Enter the no. of classes : "))
    matrix = []
     

    for i in range(no_class):
        class_i = str(input(f'Enter the predictions of class {i + 1} in each class : '))
        row = class_i.split(" ")
        row = [int(r) for r in row]
        matrix.append(row)

    print(matrix)

# calculate evaluation values
def calculate(m):

    TP = m(0,0)
    FN = m(0,1)
    FP = m(1,0)
    TN = m(1,1)

    accuracy = round((TP + TN)/(TP + TN + FN + FP),6)*100
    error_rate = round((FP + FN)/(TP + TN + FN + FP),6)*100
    precision = round(TP/(TP + FP),6)
    recall = round(TP/(TP + FN),6)
    F1_score = round(2*recall*precision/(recall + precision),6)
    precision = precision*100
    recall = recall*100

    return accuracy,error_rate,precision,recall,F1_score

get_matrix()     

