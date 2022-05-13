# File: Cipher.py

import math
# Input: str is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string

def encrypt(str):
	length=len(str)
	side=1
	while(length>side**2):side+=1

	lis=[[0 for i in range(side)]for j in range(side)]
	index=0
	for col in range(side):
		for row in range(side):
			if(index<length):lis[col][row]=str[index]
			else:lis[col][row]="*"
			index+=1

	new=[["" for i in range(side)]for j in range(side)]
	for i in range(side):
		for j in range(side):
			new[j][side-1-i]=lis[i][j]

	stringify(new)


# Input: str is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def decrypt(str):
	length=len(str)
	side=1
	while(length>side**2):side+=1
	whitespace=(side**2)-length

	starCount=0
	temp=[["" for i in range(side)]for j in range(side)]
	for i in range(side):
		for j in range(side):
			if(starCount<whitespace):
				temp[side-1-j][i]="*"
				starCount+=1
			else:break

	index=0
	for i in range(side):
		for j in range(side):
			if(temp[i][j]!="*"):
				temp[i][j]=str[index]
				index+=1

	new=[["" for i in range(side)]for j in range(side)]
	for i in range(side):
		for j in range(side):
			new[i][j]=temp[j][side-1-i]

	stringify(new)


def stringify(lis):
	str=""
	for i in range(len(lis)):
		for j in range(len(lis)):
			str+=lis[i][j]
	str=str.replace("*","")
	print(str)


def main():
	encrypt(str(input()))
	decrypt(str(input()))


main()
