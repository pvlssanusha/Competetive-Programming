"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input."""


#INPUT
candidates=[2,3,6,7]
target=7
#OUTPUT
[[2,2,3],[7]]
#CODE
res=[]
def dfs(i,cur,total):
  if total==target:
    res.append(cur.copy())
    return
  if i>=len(candidates) or total>target:
    return
  cur.append(candidates[i])
  print("currentlist1=",cur)
  dfs(i,cur,total+candidates[i])
  print("current list before poping",cur)
  cur.pop()
  print("current list after poping",cur)
  dfs(i+1,cur,total)
