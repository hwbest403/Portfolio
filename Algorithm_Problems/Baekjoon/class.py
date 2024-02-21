import sys
input = sys.stdin.readlines

class Calculator:
    def __init__(self, num):
        self.result = num
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def div(self, num):
        self.result /= num
        return self.result

Cal1 = Calculator(0)
print(Cal1.add(10))
print(Cal1.sub(5))
print(Cal1.mul(3))
print(Cal1.div(5))