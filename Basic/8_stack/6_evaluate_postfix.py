def evaluatePostfix(exp):
        st = []
        for i in exp:
            if i.isdigit():
                st.append(i)
            else:
                val1 = st.pop()
                val2 = st.pop()
                st.append(str(eval(val2 + i + val1)))
 
        return int(st.pop())
 
 
 

exp = "231*+9-"
ans = evaluatePostfix(exp)
print(ans)
