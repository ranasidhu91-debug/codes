# Task 1
def optimise_single_pickup(corridor):
    """
    This function takes in a list of numbers that represent values on a tile in a corridor and a robot is tasked to determine
    the maximum possible sum of integers possible as long as it has energy. It starts with energy 0 and is therefore unable
    to pick the first tile regardless of it's value. It obtains energy by moving to a new tile without picking up anything
    whereas it looses energy when it has picked up something. It would then return the total that was possible along with
    the values that were picked up.
    :param corridor : a list of numbers that represents the a corridor of tiles and at each index, contains a numbers
                      that corresponds to the value of the tile.
    :return         : the maximum possible value that can be obtained and a list of 1s and 0s that corresponds to the tile index.

    Complexity      : This function creates two memoization matrices of size n by n. One memoi, called memoi, keeps track of the
                      maximum possible values that can be obtained and memoi_index, which keeps track of all the indexes
                      of the tiles that were obtained to determine the maximum value. The outer loop would run n number of
                      times whereas the inner loop would run n number of times too. However, while the complexity of the
                      function is O(N^2), the previous iteration is faster than the current one. The space complexity too is
                      O(N^2)
    """
    n = len(corridor) + 1 # the length of the corridor + 1
    memoi = [[0 for x in range(n)] for y in range(n)] # memoization matrix to store the maximum possible values
    memoi_index = [[0 for x in range(n)] for y in range(n)] # matrix to store the indexes of the values that were taken
    for i in range(n-1):
        for j in range(i+1):
            memoi[i+1][j+1] = memoi[i][j] # copies the value at memoi[i][j] diagonally
            memoi_index[i+1][j+1] = memoi_index[i][j] # copies the value at memoi_index[i][j] diagonally
            # as the first row has already been memoized, there is no reason to continuously loop through it. Breaks the inner loop when i == 0
            if i == 0:
                break
            elif i == j:
                # if the value at corridor[i] is 0, there is no reason to pick it up and waste the energy.
                if corridor[i] == 0:
                    break
                # adds the values of the corridor[i] and memoi[i][j] together
                taken = memoi[i][j] + corridor[i]
                # the current value at memoi[i][j]
                not_taken = memoi[i][j]
                # gets the current value at memoi[i+1][j-1]
                current = memoi[i+1][j-1]
                # determines which one is greater, the value at memoi[i+1][j-1] or the value that was taken
                to_memoi = max(current,taken)
                # if the option to memoi is taken, then the index of it is stored in memoi_index
                if to_memoi == taken:
                    memoi_index[i+1][j-1] = i
                # memoi[i+1][j-1] = the value that was determined to be greater
                memoi[i+1][j-1] = to_memoi
                # the value that was not taken is moved diagonally downwards
                memoi[i+1][j+1] = not_taken
                # as the value was not taken, diagonally 0 is added as no value was taken
                memoi_index[i+1][j+1] = 0

                # if there was a value picked up before and there is energy left in the robot
            elif j > 0 and memoi[i][j] > 0:
                # the value at memoi[i][j] + the value at corridor[i]
                taken = memoi[i][j] + corridor[i]
                # the current value of memoi[i+1][j-1]
                current = memoi[i + 1][j - 1]
                # determines which is greater, the current value or the taken value
                value = max(taken,current)
                # stores value at memoi[i+1][j-1]
                memoi[i+1][j-1] = value
                # if value == taken, then the index is recorded in memoi_index
                if value == taken:
                    memoi_index[i+1][j-1] = i
    # the final row of memoi
    final_row = memoi[-1]
    # the final row of memoi_index
    final_row_index = memoi_index[-1]
    # creates a new list called taken_list as long as the corridor length and initiates it with 0
    taken_list = [0] * len(corridor)
    # initializaes maximum to 0
    maximum = 0
    # determines the maximum value obtained
    for i in final_row:
        if i> maximum:
            maximum = i
    # a copy of the maximum value is created
    maximum1 = maximum
    # creates a boolean value
    taken_all = False
    # determines the index of the maximum value in the final row
    maximum_index = final_row.index(maximum)
    # the maximum_index corresponds to the last index that was taken to obtain the current maximum value
    final_row_memoi_index = final_row_index[maximum_index]
    # the index that was taken is stored as 1 in taken_list
    taken_list[final_row_memoi_index] = 1
    while not taken_all:
        # using backtracking, the current maximum is determined by subtracting the value at corridor[final_row_memoi_index]
        maximum1 = maximum1 - corridor[final_row_memoi_index]
        # if maximum is lesser than 0 or 0, that means all the values have been accounted for
        if maximum1 <= 0:
            break
        # a new final row is determined that corresponds to the row which the previous index was a part of
        final_row = memoi[final_row_memoi_index]
        # the corresponding row is determined in memoi_index
        final_row_index = memoi_index[final_row_memoi_index]
        # the index of maximum1 is determined
        maximum_index = final_row.index(maximum1)
        # the value of the index that was picked up is determined
        final_row_memoi_index = final_row_index[maximum_index]
        # the index that was taken is stored as 1 in taken_list
        taken_list[final_row_memoi_index] = 1

    # the maximum value and the taken_list are returned
    return (maximum,taken_list)

# Task 2
def optimise_multiple_pickup(corridor):
    """
    This function is somewhat similar to the function above but with a minute change. The robot now is stuck in a loop.
    When it picks something up, it would continuously pick up the next items until it runs out of energy. It would still
    determine the maximum sum possible but taking the new scenario into view and still would return a list of the items that
    were picked up.
    :param corridor : a list of numbers that represents the a corridor of tiles and at each index, contains a numbers
                      that corresponds to the value of the tile.
    :return         : the maximum possible value that can be obtained and a list of 1s and 0s that corresponds to the tile index.

    Complexity      : This function creates two memoization matrices of size n by n. One memoi, called memoi, keeps track of the
                      maximum possible values that can be obtained and memoi_index, which keeps track of all the indexes
                      of the tiles that were obtained to determine the maximum value. The outer loop would run n number of
                      times whereas the inner loop would run n number of times too. However, while the complexity of the
                      function is O(N^2), the previous iteration is faster than the current one. The space complexity is
                      also O(N^2)
    """
    # length of corridor + 1
    n = len(corridor) + 1
    # memoization table to store the maximum possible values
    memoi = [[0 for x in range(n)] for y in range(n)]
    # index matrix that stores the index of the values taken
    memoi_index = [[0 for x in range(n)] for y in range(n)]
    for i in range(n - 1):
        for j in range(i + 1):
            # copies the
            memoi[i+1][j+1] = memoi[i][j] # copies the value at memoi[i][j] diagonally
            memoi_index[i+1][j+1] = memoi_index[i][j] # copies the value at memoi_index[i][j] diagonally
            if i == 0: # if the value at corridor[i] is 0, there is no reason to pick it up and waste the energy.
                break
            elif i == j:
                if corridor[i] <= 0: # if the value at corridor[i] is 0, there is no reason to initialize a pick up
                    break
                # adds the values of the corridor[i] and memoi[i][j] together
                taken = memoi[i][j] + corridor[i]
                # the current value at memoi[i][j]
                not_taken = memoi[i][j]
                # gets the current value at memoi[i+1][j-1]
                current = memoi[i+1][j-1]
                # determines which one is greater, the value at memoi[i+1][j-1] or the value that was taken
                to_memoi = max(current,taken)
                # if taken was memoized, the index is stored in memoi_index
                if to_memoi == taken:
                    memoi_index[i+1][j-1] = i
                # to_memoi is memoized to memoi[i+1][j-1]
                memoi[i+1][j-1] = to_memoi
                # the value that was not taken is moved diagonally downwards
                memoi[i+1][j+1] = not_taken
                # as the value was not taken, diagonally 0 is added as no value was taken
                memoi_index[i+1][j+1] = 0
            # if there was a value picked up before and there is energy left in the robot
            elif j > 0 and memoi[i][j] > 0:
                # determines the index of the last picked up item
                current_index = memoi_index[i][j]
                # if the item was picked up previously, the robot would not have an option now, hence diagonally downwards it would 0
                memoi_index[i + 1][j + 1] = 0
                # if the item was picked up previously, the robot would not have an option now, hence diagonally downwards it would 0
                memoi[i + 1][j + 1] = 0
                # if there was an item picked up before, the current value cannot be 0
                if current_index > 0:
                    # determines the value at memoi[i+1][j-1]
                    current = memoi[i+1][j-1]
                    # the current value at memoi[i][j] + the value at corridor[i]
                    taken = memoi[i][j] + corridor[i]
                    # if current is greater than taken, it does nothing
                    if current > taken:
                        continue
                    # stores the taken value at memoi[i+1][j-1]
                    memoi[i+1][j-1] = taken
                    # stores the index of the taken value in memoi_index
                    memoi_index[i+1][j-1] = i

    # the final row of memoi
    final_row = memoi[-1]
    # the final row of memoi_index
    final_row_index = memoi_index[-1]
    # creates a new list called taken_list as long as the corridor length and initiates it with 0
    taken_list = [0] * len(corridor)
    # initializaes maximum to 0
    maximum = 0
    # determines the maximum value obtained
    for i in final_row:
        if i > maximum:
            maximum = i
    # a copy of the maximum value is created
    maximum1 = maximum
    # creates a boolean value
    taken_all = False
    # determines the index of the maximum value in the final row
    maximum_index = final_row.index(maximum)
    # the maximum_index corresponds to the last index that was taken to obtain the current maximum value
    final_row_memoi_index = final_row_index[maximum_index]
    # the index that was taken is stored as 1 in taken_list
    taken_list[final_row_memoi_index] = 1
    while not taken_all:
        # using backtracking, the current maximum is determined by subtracting the value at corridor[final_row_memoi_index]
        maximum1 = maximum1 - corridor[final_row_memoi_index]
        # if maximum is lesser than 0 or 0, that means all the values have been accounted for
        if maximum1 <= 0:
            break
        # a new final row is determined that corresponds to the row which the previous index was a part of
        final_row = memoi[final_row_memoi_index]
        # the corresponding row is determined in memoi_index
        final_row_index = memoi_index[final_row_memoi_index]
        # the index of maximum1 is determined
        maximum_index = final_row.index(maximum1)
        # the value of the index that was picked up is determined
        final_row_memoi_index = final_row_index[maximum_index]
        # the index that was taken is stored as 1 in taken_list
        taken_list[final_row_memoi_index] = 1

    # the maximum value and the taken_list are returned
    return (maximum, taken_list)

# Task 3
def optimal_shade_selector(shades,probs):
    """
    This functions takes in two arguments, the shades and probs which are both list. The shades are the keys whereas the probs
    are the frequency with with the shades occur. This function returns the cost of the optimal decision tree.
    :param shades: the values that correspond to keys
    :param probs: the values that correspond to the frequency of the occurrence of the keys
    :return: the cost of the optimal decision tree

    Compelxity: This function first creates a N*N matrix where n is the length of the keys. It then first inserts the
                frequencies when the length of the tree is only 1 and this value corresponds to the values in the probs list.
                Then it starts making nodes of length 2 to till length n. At each node length, it determines the location
                where the memoization would be stored. It then determines the most minimal cost by changing the root nodes
                and getting values from each scenario. This function runs at a complexity of O(N*3)
    """
    n = len(probs) # length of the keys
    memoi = [[0 for x in range(n)] for y in range(n)] # creates a memoization matrix of n * n
    for i in range(n):
        # copies the frequencies when the node is only one.
        memoi[i][i] = probs[i]
    # nodes of length 2 or more.
    for chain in range(2,n+1):
        # determines the row of the node
        for i in range(n-chain+2):
            # determines the column
            j = chain+i - 1
            # breaks the loop when it's iterated the length of the table
            if i >= n or j >= n:
                break
            # initialized total cost to 0
            cost = 0
            # determines the cost of the chains
            for l in range(i,j+1):
                cost += probs[l]
            # determines the minimum value based on the root node placement.
            for k in range(i,j+1):
                # value = 0
                value = 0
                # a copy of the cost is made
                cost1 = cost
                # the cost if the next item is made the root node
                if k > i:
                    value += memoi[i][k-1]
                # the cost if the item before the last node is made root node
                if k <j:
                    value += memoi[k+1][j]
                # the total cost
                cost1 += value
                # if there is nothing stored at the memoization table, the cost is added
                if memoi[i][j] == 0:
                    memoi[i][j] = cost1
                # if there a value there, it is compared to the new cost value and if it is lower, it is stored in the table
                else:
                    if cost1 < memoi[i][j]:
                        memoi[i][j] = cost1
    # returns the optimal value for the decision tree.
    return memoi[0][n-1]