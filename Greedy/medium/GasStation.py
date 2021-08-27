# https://leetcode.com/problems/gas-station/

#https://leetcode.com/problems/gas-station/discuss/1004074/Greedy-Method-or-Explanation-%2B-Visual-or-Python


# To make a car work the difference between gas available at the gas station i.e gas[i] and the gas in the car 
# cost[i] should be positive
# Once we get this point , we can start the car 
# After starting the car can reach the destination if there is enough gas stored , 
# We keep a track of the gas in a variable trip_tank
# If the value of trip tank is positive , it means that gas is still available , so the
# trip can be completed 

def canCompleteCircuit(gas, cost):
    trip_tank = 0
    curr_tank = 0
    n = len(gas)
    for i in range(n):
	    trip_tank += gas[i] - cost[i]
	    curr_tank += gas[i] - cost[i]
	    if curr_tank < 0:
		    start = i + 1
		    curr_tank = 0 
    if (trip_tank >= 0):
        return start
    else:
        return -1