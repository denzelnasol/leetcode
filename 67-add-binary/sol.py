class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        while len(b) < len(a):
            b = '0' + b
            
        while len(a) < len(b):
            a = '0' + a
            
        result = ''
        
        a=[int(char) for char in a]
        b=[int(char) for char in b]
        
        carry = 0
        for i in range(-1, -len(a) - 1, -1):
            value = a[i] + b[i] + carry
            
            if value == 3:
                carry = 1
                result = '1' + result
            elif value == 2:
                carry = 1
                result = '0' + result
            elif value == 1:
                carry = 0
                result = '1' + result
            else:
                result = '0' + result
            
        return str(carry) + result if carry else result
            
            
            