class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol_values ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        reversed_value =s[::-1]
        total =0
        previous_value =0
        for symbol in reversed_value:
            integer_value = symbol_values[symbol]
            if integer_value < previous_value:
                total-= integer_value
            else:
                total+= integer_value
            previous_value = integer_value
        return total