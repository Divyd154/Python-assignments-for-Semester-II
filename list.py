lst = [10, 20, 30, 40]
empty_lst = []
mixed_lst = [1, "hello", 3.5, True]

print(lst[0])       
print(lst[-1])      

print(lst[1:3])     

lst.append(50)              
lst.insert(2, 25)           
lst.extend([60, 70])      

lst.remove(20)              
popped = lst.pop()          
popped2 = lst.pop(1)        
del lst[0]                  
lst.clear()                 

lst = [10, 20, 30, 20]
print(lst.index(20))        
print(lst.count(20))        

lst.sort()                  
lst.sort(reverse=True)      
lst.reverse()               