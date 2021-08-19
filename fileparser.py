class DataFile_Parser():
    def Parse_File(self):
        with open('students.dat') as fp:
            data=fp.readlines()
            q=[]
        for i in data:            
            stud=i.split(':::')
            q.append(stud)
        return q
'''st_obj=DataFile_Parser()
st_list=st_obj.Parse_File()
print (type(st_list))
for i in st_list:
     print(str(i))
     print (type(i))'''