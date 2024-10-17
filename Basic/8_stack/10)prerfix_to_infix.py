def prefix_to_infix(exp):
    s = []
    for i in exp[::-1]:
        if i.isalnum():
            s.append(i)
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.append("(" + op1 + i + op2 + ")")
    return s[0]


exp = "*-A/BC-/AKL"
result = prefix_to_infix(exp)
print(result)  

