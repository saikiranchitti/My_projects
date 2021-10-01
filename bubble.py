""" Bubble sort without using the lib function.
        Takes filename as argument.
        Sorts the numbers in the file by extracting the data in the file and cleaning.
    """


import re
import os
pattern = re.compile("^(\-?\d+\s*)+$")

# BigO time complexity O(n^2) is the average case
# BigO O(n) is the best case, where n is the number of numbers to sort
def sort_file(file):
    """ Bubble sort without using the lib function.
        Takes filename as argument.
        Sorts the numbers in the file by extracting the data in the file and cleaning.
    """
    with open(file, 'r') as file_object:
        inputfile = file_object.readlines()
        my_list=[]
        for line in inputfile:
            line=line.strip()
            arr =line.split(' ')
            for i in arr:
                if i!=' ' and i!='\n' and i!='':
                    my_list.append(int(i))
        for i in range(0,len(my_list)):
            for j in range(len(my_list)-1):   
                if(my_list[j]>my_list[j+1]):  
                    temp = my_list[j]  
                    my_list[j] = my_list[j+1]  
                    my_list[j+1] = temp
        [print(number) for number in my_list]

# BigO time complexity for the same depends on number of files starts with t5
# Hence O(M) where M is the number of files
if __name__ == "__main__":
    for file in os.listdir("."):
        if re.match("^t5.*\.dat$", file.strip()):
            sort_file(file)
        
        
