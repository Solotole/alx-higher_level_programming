#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list != []:
        new_list = []
        new_list.append(my_list[0]) # assigning to and fro first index
        for i in range(len(my_list)):
            if i == 0:
                continue
            for j in range(len(new_list)):
                if new_list[j] != my_list[i]:
                    # compare values in both lists
                    if j == len(new_list) - 1 :
                        #until it reaches the end condition
                        new_list.append(my_list[i])
                        break # if appended break inner loop
                else:
                    break # break otherwise
        for i in range(len(new_list)): # iterate throuh the list while summing
            sum += new_list[i]
    else:
        pass
    return sum
