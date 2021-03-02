#file compare
import sys
import filecmp
file1 = sys.argv[1]
file2 = sys.argv[2]
print(file1,file2)
print(filecmp.cmp(file1,file2))
print(filecmp.cmp(file1,file2,shallow=False)) # does a deep compare