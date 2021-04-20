import pickle

# d = {"name" : "tanvi","location" : "bhandup"}
# f1 = open("abcd.txt","wb")
# pickle.dump(d,f1)
# f1.close()
#
# f1 = open("abcd.txt","rb")
# d=pickle.load(f1)
# print(d)

#Store data for prime numbers in a file
def prime(x):
    for i in range(2,x):
        if x&i == 0:
            return "Its not a prime number"
            break
    else:
        return "Its a prime number"

# d={i:prime(i) for i in range(1,101)}
# f1 = open("prime.txt","wb")
# pickle.dump(d,f1)
# f1.close()

# f2=open("prime.txt","rb")
# d=pickle.load(f2)
# print(d)
