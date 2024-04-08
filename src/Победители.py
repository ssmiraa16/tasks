import collections
c=collections.Counter()

N=int(input())
for i in range(0, N):
  team=input().split(" ")
  team.sort()
  team_sorted=" ".join(team)
  c[team_sorted]+=1
  i+=1

max_wins=c.most_common()
print(max_wins[0][1])
