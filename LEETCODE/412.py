class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzBuzzList = []
        # for i in range(n):
        #     if((i+1) %3  ==0 and (i+1) %5  !=0): 
        #         fizzBuzzList.insert(i,'Fizz')
        #     elif((i+1) %5  ==0 and (i+1) %3  !=0): 
        #         fizzBuzzList.insert(i,'Buzz')
        #     elif((i+1) %5  ==0 and (i+1) %3  ==0): 
        #         fizzBuzzList.insert(i,'FizzBuzz')
        #     else: fizzBuzzList.insert(i,"{}".format(i+1))
        # return fizzBuzzList
        for i in range(n):
            if((i+1) %3  ==0 and (i+1) %5  !=0): 
                fizzBuzzList.append('Fizz')
            elif((i+1) %5  ==0 and (i+1) %3  !=0): 
                fizzBuzzList.append('Buzz')
            elif((i+1) %5  ==0 and (i+1) %3  ==0): 
                fizzBuzzList.append('FizzBuzz')
            else: fizzBuzzList.append("{}".format(i+1))
        return fizzBuzzList