def reverse_and_sum(mylist):
    sum_list=0
    reserve_list = mylist[::-1]

    for item in mylist:
        sum_list= sum_list +item

    return sum_list, reserve_list


reverse_list , sum_list = reverse_and_sum ([1,10,30])
print("sum", reverse_list)
print("revers",sum_list)