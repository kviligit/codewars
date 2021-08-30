# def each_cons(lst, n):
#     for i in range (len(lst)):
#         k = i
#         while k < len(lst)-1:
#             prntlst = []
#             for j in range (n): 
#                 prntlst.append(lst[k])
#                 k += 1
           
#         print (prntlst)
#         i += 1

# # each_cons([1,2,3,4,5], 2)

def each_cons2(lst,n):
    for i in range (len(lst)-1):
        prntlst = []
        prntlst.append(lst[i])
        k = i
        for j in range (1, n):
            k += j
            prntlst.append(lst[k])
        print(prntlst)

each_cons2([1,2,3,4,5], 2)