'''
topic:
    Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''
'''
solution1

 Useing Set
  1.Create a function to caculate the sum of the  squares of its digits
  2.Create a set to store the sum 
  3.Create a loop to judge if the Sum whether have been in  the set, if in and not is 1 return False
  other return True (if we found the 1 in the set)
'''
class Solution:
    def isHappy(self, n: int):
        resutl=set()
        while True:
            n=self.get_sum(n)
            if n==1:
                return True
            
            if n in resutl:
                return False
            else :
                resutl.add(n)
    

    def get_sum(self,n: int):
        new_sum=0
        while n:
             n,r=divmod(n,10)
             new_sum+=r**2
        return new_sum
    '''
    sloution:
    using array
    '''

    def isHappy2(self,n:int):
        record=[]
        while n not in record:
            record.append(n)
            new_num=0
            temp_str=str(n)
            for i in temp_str:
                new_num+=int(i)**2
            if new_num==1:
                return True
            else:
                n=new_num
        return False
    '''
    and we can alse use Set to store this 
    '''
    def isHappy3(self,n:int):
        record=set()
        while n not in record:
            record.add(n)
            new_num=0
            temp_str=str(n)
            for i in temp_str:
                new_num+=int(i)**2
            if new_num==1:
                return True
            else:
                n=new_num
        return False

        

           