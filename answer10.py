fruits=("apple","bannana","cherry")
y=list(fruits)
y[1]="kiwi"
fruits=tuple(y)
print(fruits)

#list mutation using slice and concat
fruits=fruits[:1]+("bannana",)+fruits[1:]
print(fruits)

tup=(0,[1,2,3])
tup[1][0]=5
print(tup[1][0:])