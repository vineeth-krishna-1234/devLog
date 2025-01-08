class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        def powCalculator(x,n):
            result =1.0
            while n:
                if n&1:
                    result*=x
                x*=x
                n=n//2
            return result
        
        return powCalculator(x,n) if n>=0 else 1.0/powCalculator(x,-n)