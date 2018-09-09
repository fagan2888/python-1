#You possess bitcoins in the form of UTXOs sorted by date and you need to send your friend X bitcoins.
#  Find a date range whose outputs that will result in the least amount of change. 
# Ideal solution will use Python whose function find_range(utxos, x) will give back the start and end dates. 
# Each utxo has value and date (in unix time).


import random
import time
import bisect

def find_range_brute_force( values, target ):
    min_sum = -1
    min_i = -1
    min_j = -1
    for i in range( len( values ) ):
        sum = 0
        for j in range( i, len( values) ):
            sum = sum + values[j]
            if sum >= target:
                if min_sum == -1 or sum < min_sum:
                    min_sum = sum
                    min_i = i
                    min_j = j
                break
    return min_i, min_j, min_sum

def find_range_windowed( values, target ):
    min_sum = -1
    min_start = -1
    min_end = -1

    sum = 0
    end = -1
    for i in range( len( values ) ):
        # advance the window by removing the first element
        if i != 0:
            sum -= values[i-1]

        # determine if we need to grow or shrink the window
        if sum == target:
            min_sum = sum
            min_start = i
            min_end = end
            break
        else:
            if sum < target:
                # grow window
                for end in range( end+1, len( values) ):
                    sum = sum + values[end]
                    if sum >= target:
                        if min_sum == -1 or sum < min_sum:
                            min_sum = sum
                            min_start = i
                            min_end = end
                        break

            else:
                # shrink window
                for end in range( end, i, -1 ):
                    sum = sum - values[end]
                    if sum < target:
                        sum += values[end] # add back in to be >= target
                        if min_sum == -1 or sum < min_sum:
                            min_sum = sum
                            min_start = i
                            min_end = end
                        break

    return min_start, min_end, min_sum

def find_range_prefix_sum( values, target ):
    min_sum = -1
    min_start = -1
    min_end = -1

    for i in range( len( values ) ):
        prefix_val = values[i]
        end = bisect.bisect( values, prefix_val + target )
        if end < len( values):
            sum = values[ end ] - prefix_val
            if sum >= target:
                if min_sum == -1 or sum < min_sum:
                    min_sum = sum
                    min_start = i
                    min_end = end - 1

    return min_start, min_end, min_sum

def find_range_timed( values, target, finder, label, iterations ):
    start = time.time()
    for i in range( iterations ):
        ret = finder( values, target)
    end = time.time()
    someString = label + ": " + `ret` + ", Time taken per iteration: " + `(end - start) / iterations`
    print(someString)
    return ret

if __name__ == "__main__":
    # use a know seed so we use the same randome sequence between runs
    random.seed( 0 )

    # create random values representing the UTXO value.  This would be just the values
    # taken from the date sorted dataset.  A prefix sum dataset is also created.
    values = []
    prefix_sum_values = []
    sum = 0
    for x in range(20000):
        v = random.random()
        values.append( v )
        prefix_sum_values.append( sum )
        sum += v
    prefix_sum_values.append( sum )

    for x in range( 10 ):
        v = random.random() * 100 # random query value between 0 and 100
        find_range_timed( values, v, find_range_brute_force,           "Brute force", 10 )
        find_range_timed( values, v, find_range_windowed,              "Windowed   ", 10 )
        find_range_timed( prefix_sum_values, v, find_range_prefix_sum, "Prefix sum ", 10 )
