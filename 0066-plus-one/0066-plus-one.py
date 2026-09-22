class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num=0
        result=[]
        for i in range(len(digits)):
            num=num*10+digits[i]

        num+=1

        while num>0:
            digits=num%10
            result.append(digits)
            num//=10
        
        result.reverse()
        return result


        