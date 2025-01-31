list1=[1, 2, 3]
list2=[4, 5, 6]
#1
list3=list1+list2

#2
list1.extend(list2)

#3
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
#['a', 'b' , 'c', 1, 2, 3]