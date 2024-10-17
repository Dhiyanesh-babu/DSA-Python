class ValidParenthesis:
    def __init__(self, s) -> None:
        self.s = s

    def check(self):
        st = []
        for ch in self.s:
            if ch in ['{', '(', '[']:
                st.append(ch)
            elif ch in ['}', ')', ']']:
                if not st:
                    return False
                if (st[-1] == '(' and ch == ')') or \
                   (st[-1] == '{' and ch == '}') or \
                   (st[-1] == '[' and ch == ']'):
                    st.pop()
                else:
                    return False
        return len(st) == 0  


def test_valid_parenthesis():
    test_cases = [
        "()",      
        "[]{}",     
        "{[()()]}", 
        "{[(])}",   
        "((()))",   
        "((({}))",  
    ]
    
    for s in test_cases:
        vp = ValidParenthesis(s)
        result = vp.check()
        print(f"Input: {s} => Valid: {result}")

test_valid_parenthesis()



        























