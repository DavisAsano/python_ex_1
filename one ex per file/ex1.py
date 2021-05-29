# part 1
# task:  L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# using both, indexing and slicing on L, assemble and print a new list N that contains:
# [0,2,3,[5,6],8,10] 
#    
# as an example, here's  how i've constructed a similar list X which contains [[2, 3], [10]] from L:
#     0    1   2          3            4
# L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
#              0 1 2 3    0    1       0 1 2
# X = [ L[2][1:-1], L[-1][2] ] 
# print(x)  => [[2, 3], [10]]
# You need to do something similar but end up with [0,2,3,[5,6],8,10] instead. One way to work 
# through this is to break the process down in small steps, store result of each step in a new variable
# and use those variables in the next step
print("start of part 1") # set breakpoint here
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print(L)
# your code
N = [L[0],L[2][1],L[2][2],[L[3][0][0],L[3][1][0]],L[4][0],L[4][2]] # create new list [0,2,3,[5,6],8,10] 
print(N)
print("end of 1") # set breakpoint here 


'''

























# solution 2
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print("L is", L)
tmp1 = L[0] # 0
tmp2 = L[2][1] # 2
tmp3 = L[2][2] # 3
tmp4 = [L[3][0][0], L[3][1][0]] # [5, 6]
tmp5 = L[4][0] # 8
tmp6 = L[4][-1] # 10 
newL = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6] # create final list
print(newL) # [0, 2, 3, [5, 6], 8, 10]
'''