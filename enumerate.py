list = [{'name':"System",'duration':'2hrs'},
        {'name':"AI",'duration':'1hrs'},
        {'name':"ML",'duration':'5hrs'}]

# for i in list:
#     print(i)  #isse mujhe indexing nhi mil rhi har ke object pe

# USE ENUMERATE

for i,video in enumerate(list,start=1):
    print(f"{i}. name={video['name']} Duration={video['duration']}")

    l=[{'name':"RUchika",'age':"21"},{'name':"Om",'age':"19"}]

l.pop(0)
print(l)