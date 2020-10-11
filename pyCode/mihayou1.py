from fractions import Fraction
# eq = input()
# stack = []
# stack.append(eq[0])
# for i in range(1, len(eq)):
#     if eq[i] == ' ':
#         continue
#     if eq[i-1]=='/' or eq[i-1]=='*':
#         fuhao = stack.pop()
#         a = eq[i]
#         b = stack.pop()
#         if eq[i-1]=='/':
#             c = float(b)/float(a)
#         else:
#             c = float(b)*float(a)
#         stack.append(c)
#     else:
#         stack.append(eq[i])
# while len(stack)>1:
#     print(stack)
#     a = stack.pop(0)
#     b = stack.pop(0)
#     c = stack.pop(0)
#     if b=='+':
#         d = float(a)+float(c)
#     elif b=='-':
#         d = float(a)-float(c)
#     stack.insert(0, d)
# print(Fraction(stack[0]))

print(Fraction(Fraction(0.2)*Fraction(0.3)))