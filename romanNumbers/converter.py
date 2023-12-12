#Sin clases
#Conversor decimales a Romanos
def decimaltoRoman(valor):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", 
        "L", "XC", "C", "CD", "D", "CM", "M"]
    romano = []
    i = 12
    while valor:
        div = valor // num[i]
        valor %= num[i]
        while div:
            romano.append(sym[i])
            div -= 1
        i -= 1
    return "".join(romano)

#Con clases
#Conversor romanos a decimales
class RomantoDecimal:
    def __init__(self, roman):
        self.values = (('M', 1000),('CM', 900),('D', 500), ('CD', 400),('C', 100),('XC', 90),('L', 50),('XL', 40),
            ('X', 10),('IX', 9),('V', 5),('IV', 4),('I', 1))
        self.result = 0
        self.list = []
        self.roman = roman

    def roman_to_int(self):
        if self.roman.upper().count("X")>3 or self.roman.upper().count("I")>3 or self.roman.upper().count("V")>3 or self.roman.upper().count("L")>3 or self.roman.upper().count("D")>3 or self.roman.upper().count("M")>3:
            print("X")
        else:
            for i in range(len(self.roman.upper())):
                for letter, value in self.values:
                    if self.roman.upper()[i] == letter:
                        self.list.append(value)
            self.list.append(0)

            for i in range(len(self.roman.upper())):
                if self.list[i] >= self.list[i+1]:
                    self.result += self.list[i]
                else:
                    self.result -= self.list[i]
        return self.result
    
if __name__=='__main__':
    pass