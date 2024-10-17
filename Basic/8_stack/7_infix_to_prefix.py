def prec(c):
    if c == '^':
        return 3
    elif c ==  '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def assoc(c):
    if c == '^':
        return 'R'
    return 'L'

def infix_to_prefix(exp):
    res = []
    st = []
    for c in exp[::-1]:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            res.append(c)
        elif c == ')':
            st.append(c)
        elif c == '(':
            while st and st[-1] != ')':
                res.append(st.pop())
            st.pop()
        else:
            while st and (prec(c) < prec(st[-1]) or (prec(c) == prec(st[-1]) and assoc(c) == 'L')):
                res.append(st.pop())
            st.append(c)
    while st:
        res.append(st.pop())
    return ''.join(res)[::-1]



exp = "(A-B/C)*(A/K-L)"

ans = infix_to_prefix(exp)
print(ans)
