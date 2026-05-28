

# Maps keys to values.

# Acronyms = { 'LOL' : 'laugh out loud',
# 'IDK' : "I Don't know",
# 'TBH' : "To be Honest"}

# Acronyms ['TBH'] = 'Honestly'
# print(Acronyms['TBH'])
# print(Acronyms)



Acronyms = { 'LOL' : 'laugh out loud',
'IDK' : "I Don't know",
'TBH' : "To be Honest"}

sentence = 'IDK' + ' what happened' + ' TBH'
translation = Acronyms.get('IDK') + ' what happened ' + Acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)
