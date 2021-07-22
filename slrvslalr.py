import ply.yacc as yacc
import ply.lex as lex

tokens = ('ID','EQUALS','STAR')

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS = r'='
t_STAR = r'\*'
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

lexer = lex.lex()

def p_statement_assign(p):
    'S : L EQUALS R'

def p_statement_R(p):
    'S : R'

def p_L_START(p):
    'L : STAR R'

def p_L_ID(p):
    "L : ID"

def p_R_L(p):
    "R : L"

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

method = input('method (LALR or SLR):')

parser = yacc.yacc(method=method, debug=True)