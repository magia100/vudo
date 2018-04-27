x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('More')


words = ['cat','dog','window','defenestrate','castrate','hipermatopeya']
print ("words: ", words)
for w in words[:]:
    if len(w) > 6:
        words.insert(-1,w)

print ("words2: ", words)
