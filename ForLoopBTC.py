

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

results = find_range_brute_force([0.3,0.5,0.1,0.6] , 0.6)
print(results)