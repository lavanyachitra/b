def reverse(sentence):
     words=sentence.split(" ")
     newwords=[word[::-1]for word in words]
     newsentence =" ",join(newwords)
     return newsentence
 sentence="Hello World"
 print(reverse(sentence))
     
