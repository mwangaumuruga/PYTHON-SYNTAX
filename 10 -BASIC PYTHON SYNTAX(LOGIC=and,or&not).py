"""this code tries to update the LOGIC conditions not included earlier which are <AND> <OR> and <Not>"""

# AND -all conditions  must be correct to ensure the condition is true
x=2==2 and 2>1
print(x)
# OR - one condition must be correct to ensure the condition is true
y=2==2 or 2>=1
print(y)
# NOT - both conditions are reversed and we get the opposite of each condition COMBINE <NOT> WITH <and &or> for it to work
z=2!=3
print(z)
A=356!=4444 and not 2>1
print(A)

