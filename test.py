from mysqldb import *

isrun1 = dbrun("insert into emp values(15,'nes')")
isrun2 = dbrun("create table emp3 (col1 int ,col2 int)")

print(isrun1)
print(isrun2)
print(all_err)
