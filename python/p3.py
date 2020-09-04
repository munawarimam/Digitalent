# No 1
def caesar_encript(txt,shift):
    result = ''   
    for i in txt:

        if i.isupper():
            i_index = ord(i)- ord('A')
            new_index = (i_index + shift) % 26 + ord('A')
            new_char = chr(new_index)
            result += new_char
        
        elif i.islower():
            i_index = ord(i) - ord('a')
            new_index = (i_index + shift) % 26 + ord('a')
            new_char = chr(new_index)
            result += new_char
        
        else:
            result += i
    return result
    
def caesar_decript(chiper,shift):
    return caesar_encript(chiper,-shift)

msg = 'Haloz DTS mania, MANTAPSZZZ!'
cpr = caesar_encript(msg,4)
txt = caesar_decript(cpr,4)

print('plain text:',txt)
print('chiper text:',cpr)


# No 2
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
 

def deshuffle_order(sftxt,order):
    sftxt_benar = [0]*len(sftxt)
    for i,j in enumerate(order):
        sftxt_benar[j] = sftxt[i]
    return ''.join(sftxt_benar)
    
print(shuffle_order('abcd',[2,1,3,0]))
print(deshuffle_order('cbda',[2,1,3,0]))

 
# No 3 
import math
def send_batch(txt,batch_order,shift=3):
    length = len(batch_order)
    batch = caesar_encript(txt, shift)
    
    count, count_size = len(batch), length
    words = [batch[i:i+count_size]for i in range (0, count, count_size)]

    for i in range(len(words)):
        words[i] += '_'*(length - len(words[i]))

    return [shuffle_order(i, batch_order)for i in words]


def receive_batch(batch_cpr,batch_order,shift=3):
    batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')

msg_cpr = send_batch("The zen of Python: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts.  Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!",[1,6,2,7,3,8,4,9,5,0],19)
msg_txt = receive_batch(msg_cpr,[1,6,2,7,3,8,4,9,5,0],19)
print(msg_txt,msg_cpr,sep='\n')


