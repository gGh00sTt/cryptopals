#this is a dump file


from helper import *

txtrd=open('encoded8.txt','r')
pt=txtrd.read().split('\n')


msg1=base64tobytes(pt)



selectedkeysize=[16,4,8]

#creating blocks
blocks=[]


for i in range(3):
    block=[]
    lengthfromtotal=1500
    noblocks=int(lengthfromtotal/selectedkeysize[i])
    if lengthfromtotal%selectedkeysize[i]!=0:
        noblocks+=1
    for j in range(noblocks):
        temp=bytes()
        for k in range(selectedkeysize[i]):
            index=j*selectedkeysize[i]+k
            if index<lengthfromtotal:
                temp+=chr(msg1[index]).encode()
        block.append(temp)

    blocks.append(block)


trnblocks=[]
trnblockslength=[]




#transponse creation
for i in range(len(blocks)):


    blocklen=len(blocks[i][0])
    trnblock=[]



    for k in range(blocklen):
        bytetrn=bytes()
        for j in range(len(blocks[i])-1):
            bytetrn+=chr(blocks[i][j][k]).encode()
        trnblock.append(bytetrn)

    trnblocks.append(trnblock)




for i in range(len(trnblocks)):
    print('keys resulting from keysize selection: ',i)
    for block in trnblocks[i]:
        #finding the keys from each block
        bytehighfreqchar=chr(bruteforcechrs(block)).encode()

        print(bytehighfreqchar.decode('utf-8'))


#Decoding the encoded ciphertext with key obtained
print('\n\nDecoded Text\n\n')

print(keyxordecode(msg1,'Terminator X: Bring the noise'.encode()).decode('utf-8'))










