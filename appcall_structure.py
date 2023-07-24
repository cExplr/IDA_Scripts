import ida_idd
# via dictionary
rec1 = {"id":1,"name":"user1"}

# Via Appcall.obj to construct object
rec2 = ida_idd.Appcall.obj(id=2, name="user2")

# Assuming there is a function that requires passing in of structure
ida_idd.Appcall.printRecord(rec1)
ida_idd.Appcall.printRecord(rec2)