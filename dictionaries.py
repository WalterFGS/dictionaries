malls = {"mall of emirates": "5km", "dubai mall": "13km", "deira mall": "7km", "marina mall": "2km"}

print(malls)
print(type(malls))

#adding items in a dictionary

malls["burj khalifa"] = "13km"
print(malls)

# print only keys or values

print(malls.keys())
print(malls.values())
print(malls.items())

#how to count items

print(len(malls))

for i in malls:
    print(i)

for i, j in malls.items():
    print(i, j)

#how to delete items

del malls["deira mall"]
print(malls)

malls["dubai mall"] = "12km"

print(malls)

---------------------------------------------------------------------------------------------------------------------------------------------------