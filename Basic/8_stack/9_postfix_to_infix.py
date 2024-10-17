def postfix_to_infix(exp) :

	s = [] 
	for i in exp:	 
		if i.isalnum():		 
			s.append(i) 
		else:
			op1 = s.pop() 
			op2 = s.pop()  
			s.append("(" + op2 + i +
							op1 + ")")  
	return s[0]


exp = "ab*c+"
ans = postfix_to_infix(exp)
print(ans)


