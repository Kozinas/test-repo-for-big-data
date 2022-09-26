######################################################
#1.1
print("1.1")
def limited_sum(my_list, n):
    sum = 0
    for x in my_list:
        if x <= n : sum += x
    return sum

print(limited_sum([1, 2, 3, 4, 5, 6, 3, 7], 7) == 31)
print(limited_sum([1, 2, 3, 4, 4, 3, 2, 1], 7) == 20)
print(limited_sum([1, 2, 3, 4, 4, 3, 2, 1], 3) == 12)
print(limited_sum([1, 2, 3, 4, 5, 6, 3, 7], 5) == 18)
print(limited_sum([1, 2, 3, 4, 5, 6, 3, 7], 3) == 9)
######################################################
#1.2
print("1.2")
def factorial(n):
    mul = 1
    for i in range(1, n + 1, 1):
        mul *= i
    return mul

print(factorial(3) == 6)
print(factorial(5) == 120)
print(factorial(9) == 362880)
print(factorial(13) == 6227020800)
######################################################
#1.3
print("1.3")
def bank(a, years, n):
    acc = a
    for i in range (years):
        acc += acc*n*0.01
    return acc

print(bank(1000, 0, 10) == 1000)
print(bank(1000, 1, 10) == 1100)
print(bank(1000, 2, 10) == 1210)
print(bank(1000, 3, 10) == 1331)
print(bank(1000, 4, 10) == 1464.1)
######################################################
#1.4
print("1.4")
def is_prime(num):
    prime = 1
    if num == 1 :
        prime = 0
    else:
        for i in range(2, num):
            if (num % i) == 0 :
                prime = 0
                break
    return prime

print(is_prime(1) == False)
print(is_prime(2) == True)
print(is_prime(17) == True)
print(is_prime(63) == False)
print(is_prime(41) == True)
######################################################
#1.5
print("1.5")
def has_dup(my_list):
    dupl = 0
    for x in my_list :
        if my_list.count(x) > 1 :
            dupl = 1
            break
    return dupl

print(has_dup([1,2,3,4,5]) == False)
print(has_dup([1,2,3,3,5]) == True)
print(has_dup([1,2,3,4,'one','two','three','four']) == False)
print(has_dup([11,2,35,4,55,15,17,3,4,35,1]) == True)
print(has_dup([1,2,3,4,'one','two','three','four','one']) == True)
######################################################
#1.6
print("1.6")
def diff(set1, set2, set3, symmetric = True):
    dataset = set()
    if symmetric == True :
        dataset = set1.symmetric_difference(set2)
        dataset = dataset.symmetric_difference(set3)
    else :
        dataset = set1.difference(set2)
        dataset = dataset.difference(set3)
    return dataset

set1 = {3, 4, 5, 6, 20}
set2 = {4, 6, 7, 8, 9}
set3 = {5, 3, 8, 1}

print(diff(set1, set2, set3) == {1, 20, 7, 9})
print(diff(set1, set2, set3, symmetric = False) == {20})
######################################################
#1.7
print("1.7")
def compare_prices(list1, list2):
    min1 = list1[0]
    max1 = list1[0]
    min2 = list2[0]
    max2 = list2[0]
    avg1 = 0
    avg2 = 0
    sum = 0
    count = 0
    str1 = ''
    str2 = ''
    str3 = ''
    
    for x in list1 :
        if max1 < x : max1 = x
        if min1 > x : min1 = x
        sum += x
        count += 1
    avg1 = sum / count
    sum = 0
    count = 0

    for x in list2 :
        if max2 < x : max2 = x
        if min2 > x : min2 = x
        sum += x
        count += 1
    avg2 = sum / count

    if avg1 == avg2 : str1 = 'Equal'
    elif avg1 > avg2 : str1 = 'Second'
    else : str1 = 'First'

    if min1 == min2 : str2 = 'Equal'
    elif min1 > min2 : str2 = 'Second'
    else : str2 = 'First'

    if max1 == max2 : str3 = 'Equal'
    elif max1 > max2 : str3 = 'Second'
    else : str3 = 'First'

    return [str1, str2, str3]

print(compare_prices([1, 2, 3], [2, 2, 2]) == ['Equal', 'First', 'Second'])
print(compare_prices([2, 2, 1], [4]) == ['First', 'First', 'First'])
print(compare_prices([3, 5], [2, 4, 6]) == ['Equal', 'Second', 'First'])
print(compare_prices([1, 7], [2, 4, 7]) == ['First', 'First', 'Equal'])
######################################################
#2.1
print('2.1')
def sorted_dept(my_list, dept):
    index = 0
    last = [None, None]
    my_list_names = list()
    my_list_debts = list()
    my_list_common = list()
    my_list.sort()

    for x in my_list :
        my_list_names.append(x[0])
        my_list_debts.append(x[1])

    for x in my_list :
        if x[0] == last[0] :
            my_list_names.pop(index-1)
            my_list_debts[index] += last[1]
            my_list_debts.pop(index-1)
            my_list.pop(index-1)
        last = x
        index += 1
    index = 0

    for x in my_list_names :
        my_list_common.append([my_list_debts[index], my_list_names[index]])
        index += 1
    index = 0

    my_list_common.sort(reverse = True)
    my_list_names.clear()

    for x in my_list_common :
        if x[0] > dept : my_list_names.append(x[1])

    return my_list_names

print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Sidorov', 4)], 1) == ['Sidorov', 'Ivanov', 'Petrov'])
print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Sidorov', 4)], 2) == ['Sidorov', 'Ivanov'])
print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Sidorov', 4)], 3) == ['Sidorov'])
print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Sidorov', 4)], 4) == [])
print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Petrov', 4)], 2) == ['Petrov', 'Ivanov'])
print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Petrov', 4)], 3) == ['Petrov'])
######################################################
#2.2
print("2.2")
def all_eq(my_list):
    max_elem = my_list[0]
    list_cp = list()
    
    for x in my_list :
        if len(x) > len(max_elem) : max_elem = x

    for x in my_list :
        list_cp.append(x + '_'*(len(max_elem)-len(x)))

    return list_cp

print(all_eq(['крот', 'белка', 'выхухоль']) == ['крот____', 'белка___', 'выхухоль'])
print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa'])
print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']) == ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____'])
######################################################
#2.3
print("2.3")
def set_gen(my_list):
    my_set = set()
    last = None
    count = None

    my_list.sort()
    for x in my_list :
        if last == x :
            count = my_list.count(x)
            for i in range(2,count+1) :
                my_set.add(str(x)*i)
            my_list.remove(x)
        my_set.add(x)
        last = x
    
    return my_set

print(set_gen([1, 1, 3, 3, 1]) == {1, 3, '111', '33', '11'})
print(set_gen([5, 5, 5, 5, 5, 5, 5]) == {'5555555', 5, '55', '55555', '5555', '555555', '555'})
print(set_gen([2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]) == {1, 2, 3, 5, 6, 7, '22', '2222', '22222', '222', '11', '222222'})
######################################################
#2.4
print("2.4")
def count_it(sequence):
    my_dict = dict()
    my_list = list()
    my_tuple = tuple()
    my_dict_len = 0

    for i in range(10) :
        my_list.append(0)

    for i in range(len(sequence)) :
        my_list[int(sequence[i])] += 1
    
    for i in range(10) :
        if my_list[i] != 0 :
            my_dict.setdefault(i, my_list[i])
    
    my_list.clear()
    my_list = (sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    my_dict.clear()
    for i in range(3 if len(my_list) >=3 else len(my_list)) :
        my_tuple = my_list[i]
        my_dict.setdefault(my_tuple[0], my_tuple[1])
    return my_dict

print(count_it('1111111111222') == {1: 10, 2: 3})
print(count_it('123456789012133288776655353535353441111') == {3: 8, 1: 7, 5: 7})
print(count_it('007767757744331166554444') == {5: 3, 7: 6, 4: 6})
######################################################
#2.5
print("2.5")
def get_most_popular(my_list, n, threshold):
    my_list_inexes = list()
    my_list_cp = list()

    for i in range(len(my_list)) :
        my_list_inexes.append(i)
    
    my_list = zip(my_list_inexes, my_list)
    my_list = sorted(my_list, key=lambda x: x[1], reverse=True)

    for x in my_list :
        if x[1] > threshold :
            if len(my_list_cp) < n :
                my_list_cp.append(x[0])

    return my_list_cp

print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 7, 1) == [7, 5, 4, 3, 2, 6, 1])
print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 7, 2) == [7, 5, 4, 3, 2, 6])
print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 3, 2) == [7, 5, 4])
print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 3, 5) == [7, 5])
print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 5, 5) == [7, 5])
######################################################