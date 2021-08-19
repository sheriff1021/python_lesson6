from student import Extended_Student
from fileparser import DataFile_Parser
from makefile import FileMaker

ps=DataFile_Parser()
listok=[]
def prepare_to():
    ks=ps.Parse_File()
    for i in ks:
        listok.append(Extended_Student(i[0],i[1],i[2],i[3],int(i[4]),i[5],i[6]))
    return listok

fm=FileMaker()
ls=prepare_to()
fm.WriteFile(ls)