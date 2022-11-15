
import re

string = input()
a = re.findall(r'X-{\\', string)
print(len(a))



# X-{\giejgiju\\\38281X-{\  - 2
# sfhwgfSHFGILSJLX-{\3@&X-{\195%X-{\jndv  - 3
# &9hdgfvhЯИТМ X-{\$hrjfheiИТМОX-{\ X-{\РВА  - 3
# ВТИТМИОСИМРЦКЫX-{\X\chs\x\[X-{\   -2
# ИТМОВТ@22@^X\{DGJF\EJGRYU%ВТИТМИОСИМРЦКЫX-{\X\chs\x\[X-{\ ВТИТМИОСИМРЦКЫX-{\X\chs\x\[X-{\   -4