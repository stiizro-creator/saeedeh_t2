def splite_even_odd(l):
    even_list=[]
    odd_list=[]
    for numbers in l:
        if numbers%2== 0:
            even_list.append(numbers)
        elif numbers%2!=0:
            odd_list.append (numbers)
    return even_list , odd_list
 
evens, odds = splite_even_odd([12, 15, 9, 10, 25])
print("Evens:", evens)
print("Odds:", odds)
