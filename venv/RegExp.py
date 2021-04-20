#Qts
# s = "Hello Where Are You From And Whats Your Name?"
#
# a=0
# b=0
# for i in s:
#     if i.islower():
#         a=a+1
#     if i.isupper():
#         b=b+1
# print(a)
# print(b)

#Check String is armstrong or not

# str = "abcdba"
# l = list(str)
# str_rev = reversed(str)
# r_l = list(str_rev)
# if l == r_l:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
#


# def almostp(s):
#     st = s
#     l = list(s)
#     re=l.reverse()
#     re="".join(l)
#     if st == re:
#         print("Its Palindrome")
#     else:
#         print("Its not Palindrome")
#
# st = input("Enter  string:")
# almostp(st)

def almostp(s):
    if len(s)<=10:
        st=s
        l=list(st)
        l1=list(st)
        l.reverse()
        mm=0
        for i in range(len(l)):
            if l[i]!=l1[i]:
                mm=mm+1
        if mm==0:
            print("Its Palindrome")
        elif mm==2:
            print("It is almost Palindrome")
        else:
            print("It is not")