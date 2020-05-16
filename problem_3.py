import sys
global huff
def huffman_encoding(data):
    char=[]
    for each in data:
        if(char.count(each)==0):
            char.append(each)
    freq=[]
    for each in char:
        freq.append(data.count(each))
    huff={}
    j=0
    for i in char:
        huff[i]=freq[j]
        j+=1
    hufftree={}
    temp='1'
    for num in sorted(huff.items(), key=lambda x:x[1]):
        hufftree[num[0]]=temp
        temp='0'+temp
        
    encode=''
    for each in data:
        encode+=hufftree[each]
    return encode, hufftree
def huffman_decoding(data,tree):
    huff = {}
    for char in tree:
        huff[tree[char]] = char

    temp = ''
    decode = ''
    for d in data:
        if d == '1':
            decode += huff[temp + d]
            temp = ''
        else:
            temp += d
    return decode
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
