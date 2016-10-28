#homework13
#Jan-Michael Carrington
#Authenticity: I certify this code is my own work.


##1. First go through the a list and find the smallest value. Swap the positions
##of that value with the beginning index. Now go through the list beginning
##with the index after the first. Find the next smallest value and swap
##it with the second position. Continue this process until the entire list
##is sorted.
##(a)
##def selectionSort(list):
##    length = len(list)
##    for i in range(length):
##        small = min(list[i:])
##        print(small)
##        index = list.index(small)
##        list[i],list[index] = list[index],list[i]
##        print(list)
##    return list
##
##def main():         
##    list=[5,2,9,7,12,8,65,3]
##    x =selectionSort(list)
##    print(x)
##main()

##2. First compare values of index 0 and 1. If index 0 is greater than 1, swap
##positions. If 1 is greater than 0, move on and compare values of 1 and 2. If
##1 is greater than 2, swap positions. If a swap occurs, begin comparisons again
##at the beginning of the list.append Repeat process until list is sorted.
##
##3. Take a list and divide the list until there remains 2 units per list. Now
##compare the values and sort each individual list. Now compare and sort the lists
##by sorting the values that were one division away from the originals. Repeat
##the process until the entire list is sorted.
##
##4.
##(a) O(n)
##(b) O(log n)
##(c) O(n^2)
##(d) O(n log n)


def baseConversion(num,base):
    first = num // base
    second = num % base
    second_str = str(second)
    if len(second_str) == 1:
        #print(first,second)
        return first, second
    first, second = baseConversion(first,second)
    return first, second
    


def main():
    a,b = baseConversion(245,16)
    print(a,b)

main()
        
    
    
