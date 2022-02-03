#  File: DNA.py

#  Description:

#  Student Name: Lauren Adams

#  Student UT EID: la27334

#  Partner Name: Siddharth Sundaram

#  Partner UT EID: svs833

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 1-18-2022

#  Date Last Modified:

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.


def main():
# read the data
#python DNA.py<dna.in
# make s1 and s2 DNA pairs from the data

  m=int(input())
  for y in range(0,m):
    str1=input()
    str2=input()
    longest_subsequence(str1,str2)

  #x=open("dna.in","r")
  #x=x.read().splitlines()

  #for i in range(1,len(x),2):
  #  longest_subsequence(x[i],x[i+1])

  #s1="ABCD"
  #s2="EFG"
  #longest_subsequence(s1,s2)

def longest_subsequence(s1,s2):
  #print(s1)
  #print(s2)
  listSubs=[]
  for x in range(len(s1)):
    for y in range(x+1,len(s1)+1):
      if(s1[x:y+1] in s2):listSubs.append(s1[x:y+1])
  #print(listSubs)

  if(len(listSubs)>0)and(len(max(listSubs,key=len))>1):
    longest=len(max(listSubs,key=len))
    longSubs=[]
    for i in range(len(listSubs)):
       if(len(listSubs[i])==longest):longSubs.append(listSubs[i])
    longSubs=list(set(longSubs))
    longSubs.sort()
    print(*longSubs,sep="\n")
  else:print("No Common Sequence Found")
  print()

main()

  #if(len(listSubs)>0):
  #  longest=len(max(listSubs,key=len))
  #  if(longest>1):
  #    longSubs=[]
  #    for i in range(len(listSubs)):
  #      if(len(listSubs[i])==longest):longSubs.append(listSubs[i])
  #    longSubs = list(set(longSubs))
  #    print(*longSubs,sep="\n")
  #  else:print("No Common Sequence Found")
  #else:print("No Common Sequence Found")

  ### extra credit ###
  #longSubs=list(set(longSubs))
  #if(len(longSubs)>0):print(*longSubs,sep="\n")
  #else:print("No Common Sequence Found")

# for i in range(len(listSubs)):
#  if(len(listSubs[i])>longest):
#    longest=len(listSubs[i])