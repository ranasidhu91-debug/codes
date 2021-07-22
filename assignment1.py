from timeit import default_timer as time
import random
import csv
## Task 1
def  numerical_radix_sort(num_list,b):
    """
    This function performs a radix sort by taking in two arguments, num_list that is a list of numbers in base 10
    and b which is the base in which the numbers would be sorted in. The list is sorted by using each integer as a column
    and sorted from right to left.
    Precondition: the list must be integers and the base must be an integer value.
    :param num_list : unsorted positive list of integers with base 10
    :param b        : Base in which num_list would be sorted by
    Time Complexity : The complexity of maximum is 0(n) whereas the complexity of the maximum number of columns is O(m).
                      For each column, counting_sort_stable function is called, making the complexity of this function
                      as 0(n + m + m(n+b)) = 0(m(n+b)). Best case = worst case as there is no avenue for the while loop to
                      terminate earlier.

    :return: a sorted list
    """
    # finding the maximum value in num_list
    maximum = get_max(num_list)
    # determines the maximum number of columns based on the base.
    max_columns = 0
    while b**max_columns <= maximum:
        max_columns += 1
    col_iter = 0
    # a conditional while loop is used to iterate until the maximum number of columns have been iterated.
    while col_iter < max_columns:
        # performs the radix sort
        num_list = counting_sort_stable(num_list,col_iter,b)
        col_iter += 1
    return num_list

def get_index(base,column,item):
    """
    This function determines the index in which the integer would be placed in the bucket.
    :param base     : base in which the sorting should happen
    :param column   : the column in item that needs to be sorted
    :param item     : the item that is to be sorted
    :return         : index value of the integer in column
    """
    return (item//(base**column)) % base

def counting_sort_stable(unsorted,column,base):
    """
    This function is called by numerical_radix_sort. It takes in a list of unsorted integers and determines the column that
    needs to be sorted according to the base that is being required. A list count_array is created according to the base
    and the indexes of the columns is determined and stored in the count_array. Then the count_array is iterated and the indexes
    that contain the numbers would then be added into sorted accordingly to maintain stability.
    Pre-condition       : unsorted must be a list of positive integers, column and base must be integers too
    :param unsorted     : unsorted list of numbers
    :param column       : column to iterate
    :param base         : the base used to sort
    Time Complexity     : Count_array gives a complexity of O(b) where b is the base. Sorted is created by
                          having the outer loop of count_array and then adding the items in the count_array while maintaining
                          the stability of the array. Therefore, the complexity of the function is O(n+b).
    :return: sorted array
    """
    # count_array is created according to the base
    count_array = [None] * (base)
    # empty lists are added into the count_array
    for i in range(len(count_array)):
        count_array[i] = []
    # count_array is updated with the items in unsorted.
    for item in unsorted:
        index = get_index(base,column,item)
        count_array[index].append(item)
    # a new list is created which stores the sorted items while maintaining the stability
    sorted = []
    for i in count_array:
        if len(i) != 0:
            for j in range(len(i)):
                sorted.append(i[j])
    return sorted

def get_max(list1):
    """
    This function determines the maximum value in list1
    Pre-condition   : unsorted list of positive integers
    :param list1    : unsorted list of positive integers
    Time-Complexity : O(n) where n is the number of items in list1
    :return         : maximum value in the list
    """
    if len(list1) == 0:
        return 0
    maximum = list1[0]
    for i in list1:
        if i > maximum:
            maximum = i
    return maximum
#
# print("Task 1")
# numbers = [9000,608,89432,7821,65]
# print(numbers)
# print(numerical_radix_sort(numbers,10))

## Task 2
def test_bases(num_list):
    """
    This function takes in an unsorted list of positive integers, determines the time taken for radix sort
    to sort the list using a base of 2^exponent where exponent is 1 and adds the value of the exponent and
    time taken into the list, value as a tuple. A while loop is then used where the loop would stop when all-time exceeds
    the time taken to radix sort with exponent 1. The exponents would continue to increase by 1 until the loop stops.
    Pre-condition   : Num_list is a list of positive unsorted integers
    :param num_list : list of positive unsorted integers

    Time-Complexity : This function calls numerical_radix_sort n number of times. Therefore the complexity
                      of this function is O(n) * O(m(n+b)).
    :return: a list containing the tuple of [exponent,time taken]
    """
    value = []
    exponent = 1
    # start time
    start = time()
    numerical_radix_sort(num_list,2**exponent)
    # end time
    end = time()
    # time taken to sort num_list
    time_taken1 = end-start
    value.append([exponent,time_taken1])
    all_time = 0
    while all_time < time_taken1:
        exponent += 1
        start = time()
        numerical_radix_sort(num_list,2**exponent)
        end = time()
        all_time = end - start
        if all_time > time_taken1:
            break
        value.append([exponent,all_time])
    
    return value
#
# print("Task 2")
# random.seed(0)
# data1 = [random.randint(0,2**8-1) for _ in range(10**4)]
# print(test_bases(data1))

## Task 3

def scrabble_helper(word_list,char_set_list):
    """
    This function takes in a list of words, word_list and a list of strings,char_set_list. For each string in char_set_list,
    it would return a list sorted alphabetically that serve as an anagram of the string that exists in the word_list.
    It returns a list of list.
    Pre-condition       : The string must be in lowercase and the strings can be of any length
    :param word_list    : unsorted list of strings
    :param char_set_list: List of words that need to have their anagrams present in word_list
    Time-Complexity     : As this is a culmination of all the other functions and the loop iterates i number of times where
                          i is the length of words in char_set_list, the complexity of this is O(nM + iMlog(n))
    :return: list of list that contains the anagrams of each word in char_set_list
    """
    # a list of indexes is created
    if len(word_list) == 0:
        array = [None] * len(char_set_list)
        for i in range(len(array)):
            array[i] = []
        return array
    indexes = index_list(word_list)
    # word list is sorted according to the length of the words first
    word_list = preprocessing(word_list,indexes)
    anagram_words = []
    # the list of words that serve as anagram to the words in char_set_list is created.
    for i in char_set_list:
        if len(i) == 0:
            continue
        anagram = search_words(word_list,i)
        anagram_words.append(anagram)
    return anagram_words

def index_list(list1):
    """
    This function takes in a list of unsorted words and generates a index array which contains the length of the words.
    :param list1    : Unsorted words
    Time Complexity : This function has a complexity of O(n) as it iterates through list1 n number of times where n is the
                      length of the array indexes.
    :return         : index array containing the length of the words in list1
    """
    indexes = [None] * len(list1)
    for i in range(len(indexes)):
        indexes[i] = len(list1[i])
    return indexes

def search_words(sorted_length,word):
    """
    This function takes in a list of words that are sorted according to their lengths, sorted_length and the word to determine
    if it's anagram is present in sorted_length.
    Pre-condition       : Words sorted according to length and one word.
    :param sorted_length: List of words sorted according to length
    :param word         : A string of word.
    Time - Complexity   : This function first calls index_list which has a Complexity of O(n). Then it calls binary_search
                          which has a complexity of O(log N). It then calls counting_sort 2i number of times. Therefore,
                          the complexity so far is O(n) + O(log N) + [O(i) * O(n+b)). Finally, the while loop iterates
                          according to the max columns, m number of times. So the final complexity of this would be
                          O(m*(n + logN))
    :return             : List containing the anagrams of word that are present in sorted_length
    """
    # indexes of the length of the words is created
    indexes = index_list(sorted_length)
    # the first index of the word with the same length as length_of_word is determined
    first_index = binary_search(indexes,len(word),True)
    # the last index of the word with the same length as length_of_word is determined
    last_index = binary_search(indexes,len(word),False)
    anagrams = []
    # the words containing the anagrams of word in sorted_length are added into anagrams.
    for i in range(first_index,last_index+1):
        words = sorted_length[i]
        # if the length matches but they are not the same letters, words is not added into anagram
        words_sorted = counting_sort_word(words)
        word_sorted = counting_sort_word(word)
        if words_sorted == word_sorted:
            anagrams.append(words)
    if len(anagrams) == 0:
        return anagrams
    else:
        max_columns = len(anagrams[0])
        if len(anagrams) == 1:
            return anagrams
        else:
            # the words are sorted in alphabetical order
            while max_columns > 0:
                anagrams = counting_sort_string(anagrams,max_columns)
                max_columns -= 1
    return anagrams

def counting_sort_string(unsorted,col):
    """
    This function accepts a list of unsorted words and takes in a value of the column to iterate over and
    returns an array of words that are sorted in an alphabetical order according to the column that it is.
    Pre-condition   : An unsorted list of words and the value of column must be an integer
    :param unsorted : Unsorted list of words
    :param col      : The column to iterate over
    Time-Complexity : This function first creates an array of length b and then iterates through the loop b number of times,
                      giving it a complexity of O(b)  It then sorts the strings using left indentation and using the last
                      letters as the starting point which has a complexity of O(n) where n is the length of unsorted list.
                      Within the loop itself, it calls the string_ascii function that has a complexity of O(1). Lastly,
                      Sorted is created by iterating over the outer loop of array and then adding the items in the array
                      while maintaining the stability of the array. Therefore, the complexity of the function is O(n+b).
    :return         : Alphabetically sorted words.
    """
    array = [None] * 27
    for i in range(len(array)):
        array[i] = []
    for i in range(len(unsorted)-1,-1,-1):
        item = unsorted[i]
        if col > len(item):
            index = 0
        else:
            index = string_ascii(item,col) + 1
        array[index].append(item)
        index += 1
    sorted = []
    for i in array:
        if len(i) != 0:
            for j in range(len(i)):
                sorted.append(i[j])
    return sorted

def preprocessing(word_list,indexes):
    """
    This function sorts the list of words according to their lengths in increasing order and takes in two arguments, an
    unsorted list, word_lists and a list of indexes.
    Pre-Condition   : Unsorted list of words,list of indexes containing the lengths of the words in word_list
    :param word_list: Unsorted list of words
    :param indexes  : List containing the length of the words in word_list.
    Time-Complexity : As this is very much similar to counting_sort_stable, it has the same complexity as counting_sort_stable
                      which is O(b+n)
    :return: A sorted list containing the words in ascending order of length
    """
    maximum = get_max(indexes)
    array = [None] * (maximum + 1)
    for i in range(len(array)):
        array[i] = []
    for item in word_list:
        index = len(item)
        array[index].append(item)
    sorted = []
    for i in array:
        if len(i) != 0:
            for j in range(len(i)):
                sorted.append(i[j])
    return sorted

def string_ascii(word,col):
    """
    This function takes in a word and determines the index value of the column of the particular word by using ord and then
    subtracting by 97.
    :param word     : a string of word
    :param col      : Column to be iterated
    Time-Complexity : O(1) as all operations are constant.
    :return         : Integer value that serves as an index for the letter.
    """
    index = ord(word[col-1]) - 97
    return index

def counting_sort_word(word):
    """
    This function sorts the letters in a word in an ascending manner
    :param word     : a word that needs to be sorted
    Time-Complexity : Final_array is created by iterating over the outer loop of count_array n numbers of times and then
                      adding the items in the count_array b number of times while maintaining the stability of the array.
                      Therefore, the complexity of the function is O(n+b)
    :return         : the word sorted in alphabetical order
    """
    # maximum is initialised
    maximum = ord(word[0]) - 97
    for i in word:
        i = ord(i) - 97
        if i > maximum:
            maximum = i
    # empty count_array is created of length maximum + 1
    count_array = [None] * (maximum+1)
    for i in range(len(count_array)):
        count_array[i] = []
    # the letters in word are treated individually and added accordingly to their index value into count_array
    for item in word:
        i = ord(item) - 97
        count_array[i].append(item)
    # final_array is created by adding the sorted items into it from count_array
    final_array = []
    for i in count_array:
        if len(i) != 0:
            for j in range(len(i)):
                final_array.append(i[j])
    return final_array

def binary_search(indexes,length_of_word,searchFirst):
    """
    This function takes in a list that contains the length of the words as indexes, indexes and takes in the length of the
    word to be searched for, length_of_word and a boolean value of true or false. If the boolean value is true, it would
    return the index of the first occurrence of the word with same length and if the boolean value is false, the last index.
    :param indexes          : A list containing the length of the words.
    :param length_of_word   : The length of the word being searched.
    :param searchFirst      : a Boolean value of true or false.
    Time-Complexity         : This function has a complexity of O(log N) as after each iteration, it is halving the value of
                              n.
    :return                 : First or last index of the occurrence of length_of_word
    """
    low = 0
    high = len(indexes) - 1
    result = -1
    while low <= high:
        mid = (high + low) // 2
        # if indexes[mid] == length_of_word, result would be mid
        if indexes[mid] == length_of_word:
            result = mid
            # if searchFirst is true, then high would keep reducing until it reaches the first index of that matches length_of_word
            if searchFirst:
                high = mid - 1
            else:
                # if searchFirst is false, then low would keep on increasing until it reaches the last index that matches length_of_word
                low = mid + 1
        elif length_of_word < indexes[mid]:
            high = mid -1
        else:
            low = mid + 1
    return result

# random.seed(0)
# data1 = [random.randint(0,2**8-1) for _ in range(10**4)]
# data2 = [random.randint(0,2**8-1) for _ in range(10**5)]
# data3 = [random.randint(0,2**(2**10)-1) for _ in range(10)]
# data4 = [random.randint(0,2**(2**10)-1) for _ in range(20)]
#
# data_set = [data1,data2,data3,data4]
#
# def main():
#     with open("charts.csv","w",newline="") as file:
#         writer = csv.writer(file)
#         for i in data_set:
#             values = test_bases(i)
#             for j in values:
#                 writer.writerow(j)
#
#
# if __name__ == '__main__':
#     main()

words = ["strut", "trust", "tutor", "trout", "slut", "rstut", "rtsut", "rotut", "rotor","rotur"]


num_list = [123,312,1000,76,594,100]
b = 3

numerical_radix_sort(num_list,b)



