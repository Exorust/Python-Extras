import textract
import operator

file='/home/chandrahas/Downloads/idiot.pdf'
text = str(textract.process(file, encoding='ascii'))
print(text)

text_final=[]
word_count={}
sortings={}
def strip(texting):
    text1= texting.lower().split()
    for t in text1:
        text2= t.split('\\n')
        for tt in text2:
            if tt is not '':
                text_initial.append(tt)

    for word in text_initial:
        waste = "`~!@%#$%^&*()1234567890-_=+\][|}{';\":/.,?><"
        for i in range(0,len(waste)):
            word=word.replace(waste[i], '')
        if len(word) > 0:
            text_final.append(word)
    for words in text_final:
        if words in word_count:
            word_count[words] = word_count[words]+ 1
        else:
            word_count[words] = 1


    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


strip(text)