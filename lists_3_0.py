user_string=input('enter string: ')
user_word=input('enter word you wanna count: ')
word=user_string.split()
amount=0
for w in word:
    if w==user_word:
        amount+=1
print('amount of', user_word, 'is:', amount)


