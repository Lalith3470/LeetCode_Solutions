class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic={}
        ch=97
        for i in range(len(key)):
            if key[i] not in dic and key[i]!=" ":
                dic[key[i]]=chr(ch)
                ch+=1
        st=""
        for i in range(len(message)):
            if message[i]==" ":st+=" "
            if message[i] in dic:st+=dic[message[i]]
        return st
