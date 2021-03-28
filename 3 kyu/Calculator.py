from operator import add, sub, mul, truediv


class Calculator:

    def __init__(self):
        self.result = []
        self.ops = {'+': add, '-': sub, '*': mul, '/': truediv}
        self.parens = 0
        self.inner_value = 0

    def evaluate(self, string):
        string = self.handle_parens(string)
        self.result = string.split(' ')
        self.check_next('*/')
        self.check_next('+-')
        return float(self.result[0])

    def handle_parens(self, string):
        self.parens = string.count('(')

        while self.parens:
            l_paren = string.rfind('(')
            r_paren = string.find(')', l_paren)
            eq = string[l_paren + 1:r_paren - 1].split()
            print(eq)
            if len(eq) == 1:
                self.inner_value = float(eq[0])
            elif len(eq) > 1:
                self.inner_value = self.ops[eq[1]](float(eq[0]), float(eq[2]))

            string = string[:l_paren] + str(self.inner_value) + string[r_paren + 1:]
            self.parens -= 1

        return string

    def check_next(self, op):
        s = 1
        while s < len(self.result) - 1:
            if self.result[s] in op:
                self.result[s - 1] = str(self.ops[self.result[s]](float(self.result[s - 1]),
                                                                  float(self.result[s + 1])))
                self.result.pop(s + 1)
                self.result.pop(s)
                continue
            s += 1


q = '2 * 5 * 3 * 1 / 2'
p = '( ( ( ) ) ( ( ( 255 * 1444 ) ) ) ) )'
calc = Calculator()
print(calc.evaluate(p))
