#knapsackDP.knapsackDP(8,[3,8,5], [4,6,5])
#objective value:  9.0
#combinations are:  [1, 0, 1]
#
#knapsackDP.knapsackDP(4,[2,3,1], [31,47,14])
#objective value:  62.0
#combinations are:  [2, 0, 0]
#
#knapsackDP.knapsackDP(22,[15,10,18], [24,15,25])
#objective value:  30.0
#combinations are:  [0, 2, 0]
#
#knapsackDP.knapsackDP(69,[14,10,12,25,20], [42,26,35,71,53])
#objective value:  203.0
#combinations are:  [4, 0, 1, 0, 0]
#
#knapsackDP.knapsackDP(10,[3,4,1,7], [7,9,2,15])
#objective value:  23.0
#combinations are:  [2, 1, 0, 0]

import knapsackDP as knapsackDP

reload(knapsackDP)

#final = knapsackDP.knapsackDP(8,[3,8,5], [4,6,5])
#final = knapsackDP.knapsackDP(22,[15,10,18], [24,15,25])
#final = knapsackDP.knapsackDP(4,[2,3,1], [31,47,14])
#final = knapsackDP.knapsackDP(69,[14,10,12,25,20], [42,26,35,71,53])
final = knapsackDP.knapsackDP(10,[3,4,1,7], [7,9,2,15])

print 'objective value: ', final.f
print 'combinations are: ', final.result
