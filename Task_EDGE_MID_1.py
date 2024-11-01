
#defining the function for all the expected pairs in the list
def claculate_pair(list,target_value):

    size_list=len(list)
    result_pair=[]
    result_list=[]
    

    for i in range(0,size_list-1):
        for j in range(1,size_list):
            if list[i]+list[j] == target_value:
                print(f'{list[i]},{list[j]}')
            


#taking input the target value

target_value=int(input('Enter the Target Value: '))

#define the list size
list_size = int(input("enter the size of list: "))



#taking input the list of numbers
number_list=[]
for i in range(0,list_size):
    number=int(input('Enter the element: '))

    number_list.append(number)


#caling the function
claculate_pair(number_list,target_value)