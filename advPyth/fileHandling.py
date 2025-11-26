# # f=open("s_g.py","r")
# # xyz=f.read()
# # # print(xyz)

# # d=open("vamsiResume.txt","w")
# # abc=d.write("vamsi@gmail.com")
# # print(abc)


# # e=open("vamsiResume.txt","r+")
# # print(e.read()) # vamsi@gmail.com

# # e.write("\n1234567890") # 1234567890
# # print(e.read()) # vamsi@gmail.com 123456789

# # m=open("vamsiResume.doc","r+")
# # abc=m.read()
# # m.write("\n123456789")
# # print(abc)


# # k=open("vamsiResume.pdf","r+")
# # abc=k.read()
# # k.write("\n123456789")
# # print(abc)

# # a=open("vamsi.txt","w+")
# # a.read()
# # a.write("vamsi")
# # print(a.read())



# # a=open("vamsi.txt","w")
# # a.write("vamsiiiii1234567890i")



# # aabc=open("vamsi.txt","a")
# # aabc.write("\n10000coders")

# a=open("vamsi.txt","x")
# a.write("asdfghj")

# # a
# # r
# # w 
# # r+
# # w+
# # x :-- if file is there, you will get rror

# a=open("data.json","w")
# name="vamsi"
# age=27
# a.write(f"name: {name} , age:{age}")


# import json


# email="ramesh@gmail.com"
# pswd="1234567"

# cred={
#     "email":email,
#     "password":pswd
# }

# with open("users.json","a") as f:
#     json.dump(cred,f)

import json


# with open("registedUsers.json","w") as f:
#     json.dump([],f)
email=input("enetr enmail here :--  ")
pswd=input("enter pasword here :--  ")
new_user={
    "email":email,"pswd":pswd
}

with open("registedUsers.json","r") as f:
    r_users=json.load(f)
    print(r_users)
r_users.append(new_user)    

with open("registedUsers.json","w") as f:
    json.dump(r_users,f)