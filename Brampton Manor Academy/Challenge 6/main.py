#Challenge 6

def square(order):
    k = order + 1
    for i in range(1, k):
        temp = k
        while (temp <= order) :
            print(temp, end = " ")
            temp += 1
         
        for j in range(1, k):
            print(j, end = " ")
 
        k -= 1
        print()

square(5)