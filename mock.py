# ============================
# WeThinkCode Mock Test 3
# ============================

# Question 1
def nested_sum(lst):
    if not lst:
        return 0
    total =  0
    for i in lst:
        if  not isinstance(i,list):
            total += i
        if isinstance(i,list):
            total += nested_sum(i)

    return total

print(nested_sum([1, [2, 3], [4, [5]]]))

 
# Question 2
def reverse_dict(d):
    dict = {}
    for key,value in d.items():
        if value in dict:
          dict[value].append(key)
        else:
            dict[value] = [key]
    return dict

print(reverse_dict({'a':1,'b':2,'c':1}))


# Question 3
def is_fibonacci(n):

    pass




# Question 4
def deep_flatten(lst):
    flats = []
    for i in lst:
     if not isinstance(i,list):
         flats.append(i)
     else:
         flats.extend(deep_flatten(i))
         
    return flats
    
print(deep_flatten([1, [2, [3, 4], 5], 6]))
# Question 5
def pyramid_pattern(s):
    string=''
    for i in range(len(s)):
        for x in range(i):
            print(s[x], end='') # WHY THE FUCK ISNT IT WORKINGF

    
from collections import Counter
# Question 6
def max_consecutive(lst):
    if not lst:
        return 0
    return max(dict(Counter(lst)).values())
    

# Question 7
def filter_dict(d, threshold):
    new_d = d.copy()
    for key, value in d.items():
        if value < threshold:
            del new_d[key]
    return new_d

# Question 8
def max_depth(lst):
    if not lst:
        return 0
    new = []

    for i in lst:
        if  not isinstance(i,list):
            new.append(1)
        if isinstance(i,list):
           new.append( len(nested_sum(i)))

    return max(new)
# print(max_depth([1, [2,3], [4, [5]]]))

# Question 9
def reverse_words_rec(sentence):
    sen= sentence.split()
    if len(sentence) < 2:
        return sentence
    else:
        return reverse_words_rec(sen[len(sen ) -1]) # OMG i am so fucked for my upcoming test



# Question 10
def column_sum(matrix):
    if not matrix:
        return []
    lst = []
    for row in range(len(matrix)):
        sums = 0
        for col in range(len(matrix)):
            sums += matrix[col][row]
        lst.append(sums)
    return lst
print(column_sum([[1,2,3],[4,5,6],[7,8,9]]))
    