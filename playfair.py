def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y
matrix=[]
plaintext=input('Enter plaintext::')
plaintext=plaintext.upper();
#print(plaintext.upper())

keyword=input('Enter keyword::')
keyword=keyword.upper()
#plaintext='GOODMORNINGALL'
#keyword='MONARCHY';
alpha='abcdefghijklmnopqrstuvwxyz'
alpha=alpha.upper()
#creating martix
for e in keyword.upper():
    if e not in matrix:
        matrix.append(e)

print('KeyWord',matrix)

for e in alpha:
    if e not in matrix:
        if e=='J':
            x='hello'
        else:
            matrix.append(e)
    

keyword_matrix=[]
for e in range(5):
    keyword_matrix.append('')
    
keyword_matrix[0]=matrix[0:5]
keyword_matrix[1]=matrix[5:10]
keyword_matrix[2]=matrix[10:15]
keyword_matrix[3]=matrix[15:20]
keyword_matrix[4]=matrix[20:25]


print('KeyWord Matrix 5*5(KEY)',keyword_matrix)

#plaintext
message=[]
for  plain in plaintext:
    message.append(plain)
for unused in message:
    if unused== '':
        message.remove('')
#even length
print('message(PLAINTEXT)',message)
i=0
l=int(len(message)/2)

for both in range(l):
    if message[i]== message[i+1]:
        message.insert(i+1,'X')
    i=i+2
#odd length
if len(message)%2==1:
    message.append("X")
i=0
new_message=[]
l=int(len(message)/2)+1
#l=int(len(message))/2+1)

for x in range(1,l):
    new_message.append(message[i:i+2])
    i=i+2    
print(new_message)
q=0;
cipher_matrix=[]
for e in new_message:
    p1,q1=find_position(keyword_matrix,e[0])
    p2,q2=find_position(keyword_matrix,e[1])
    
    if p1==p2:
            if q1==4:
                    q1=-1
            if q2==4:
                    q2=-1
            cipher_matrix.append(keyword_matrix[p1][q1+1])
            cipher_matrix.append(keyword_matrix[p1][q2+1])
    elif q1==q2:
            if p1==4:
                    p1=-1;
            if p2==4:
                    p2=-1;
            cipher_matrix.append(keyword_matrix[p1+1][q1])
            cipher_matrix.append(keyword_matrix[p2+1][q2])
    else:
           cipher_matrix.append(keyword_matrix[p1][q2])
           cipher_matrix.append(keyword_matrix[p2][q1])
print(str(cipher_matrix))
str1=''.join(cipher_matrix)
i=0
new_cipher_matrix=[]
for x in range(int(len(cipher_matrix)/2)):
        new_cipher_matrix.append(cipher_matrix[i:i+2])
        i=i+2
print(new_cipher_matrix)
omessage=[]
for e in new_cipher_matrix:
		p1,q1=find_position(keyword_matrix,e[0])
		p2,q2=find_position(keyword_matrix,e[1])
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			omessage.append(keyword_matrix[p1][q1-1])
			omessage.append(keyword_matrix[p1][q2-1])		
		elif q1==q2:
			if p1==4:
				p1=-1;
			if p2==4:
				p2=-1;
			omessage.append(keyword_matrix[p1-1][q1])
			omessage.append(keyword_matrix[p2-1][q2])
		else:
			omessage.append(keyword_matrix[p1][q2])
			omessage.append(keyword_matrix[p2][q1])

for unused in range(len(omessage)):
        if "X" in omessage:
                omessage.remove("X")
print("oringal Message")
print(omessage)
