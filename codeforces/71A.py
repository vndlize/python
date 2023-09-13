word_count = int(input())
words = []
for i in range ( word_count ) :
    word = input()
    words.append(word)
for i in words :
    if len(i) > 10 :
        print (f'{i[0]}{len(i)-2}{i[-1]}')
    else :
        print (i)
