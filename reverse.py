import math
def checkPalindrome(inputString):

        if 1<=len(inputString)<=10**5:
            k = 1
            for i in range(math.floor((len(inputString)/2))):
                if inputString[i] == inputString[len(inputString)-1-i]:
                    k *= 1
                else: k*= 0
        if k==0:
            return False
        else:
            return True
print(checkPalindrome("aabaa"))
                    


