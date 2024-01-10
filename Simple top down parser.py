class Parser:
    def __init__(self, input_string):
        self.tokens = input_string.split()
        self.current_token = None
        self.index = 0

    def get_next_token(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
        else:
            self.current_token = None

    def parse(self):
        self.get_next_token()
        self.expression()

    def expression(self):
        self.term()
        while self.current_token in ['+', '-']:
            operator = self.current_token
            self.get_next_token()
            self.term()
            print(f' {operator} ', end='')

    def term(self):
        self.factor()
        while self.current_token in ['*', '/']:
            operator = self.current_token
            self.get_next_token()
            self.factor()
            print(f' {operator} ', end='')

    def factor(self):
        if self.current_token.isdigit():
            print(self.current_token, end='')
            self.get_next_token()
        elif self.current_token == '(':
            self.get_next_token()
            self.expression()
            if self.current_token == ')':
                self.get_next_token()
            else:
                raise SyntaxError("Expected ')'")
        else:
            raise SyntaxError("Invalid token")

# Example usage
input_string = "3 + 4 * ( 2 - 1 )"
parser = Parser(input_string)
parser.parse()
