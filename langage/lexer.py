import ply.lex as lex

class Lexer:
    # List of token names.   This is always required
    tokens = (
       'NUMBER',
       'PLUS',
       'MINUS',
       'TIMES',
       'DIVIDE',
       'LPAREN',
       'RPAREN',

       'ID',
       'ASSIGN'
    )

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

    t_ASSIGN = r'='

    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|_|[0-9])*'
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s' at position %d" % (t.value[0], t.lexpos))
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(object=self, **kwargs)
        return self

    def test(self):
        # Build the lexer
        lexer = lex.lex()
        lexer.input('''3 + 4 * 10
                + 4 - 20 * 12''')
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break      # No more input
            print(tok)

if __name__ == '__main__':
    lexer = Lexer().build()
    lexer.lexer.input('''
    a = 3
    ''')
    for token in lexer.lexer:
        print(token)
