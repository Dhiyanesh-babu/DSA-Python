def evaluatePrefix(exp):
        st = []
        for i in exp[::-1]:
            if i.isdigit():
                st.append(i)
            else:
                val1 = st.pop()
                val2 = st.pop()
                st.append(str(eval(val1 + i + val2)))
 
        return int(st.pop())
 
 
 

exp = "+9*26"
ans = evaluatePrefix(exp)
print(ans)