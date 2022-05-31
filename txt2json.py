import re
import json
from copy import deepcopy

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
ret = {}
data = long_text.strip().split("\n")
# print(data)
N = len(data)
ret['name'] = data[0]
ret['lei'] = data[1]

tmp0 = []
flag = 0
tmp1 = {}
for i, it in enumerate(data[2:]):
    regex = re.search(r"^\d+?\.\s(.+)", it)
    if regex:
        if flag == 0:
            # 判断首部
            tmp1 = {"title": regex.group(1), 'isin': []}
            flag = 1
        elif flag == 1:
            # 到达第二段
            tmp0.append(deepcopy(tmp1))
            tmp1 = {"title": regex.group(1), 'isin': []}
            flag = 1
    elif re.match(r'\w+', it):
        # 满足数据条件
        tmp1['isin'].append(it)
    if i == N - 3:
        # 判断尾部
        tmp0.append(deepcopy(tmp1))

ret['sub_fund'] = tmp0
print(json.dumps(ret, sort_keys=True, indent=4, separators=(',', ':')))

'''
{
    "lei":"529900LPCSV88817QH61",
    "name":"Variopartner SICAV",
    "sub_fund":[
        {
            "isin":[
                "LU2001709034",
                "LU2057889995",
                "LU2001709547"
            ],
            "title":"TARENO GLOBAL WATER SOLUTIONS FUND"
        },
        {
            "isin":[
                "LU1299722972"
            ],
            "title":"TARENO FIXED INCOME FUND"
        },
        {
            "isin":[
                "LU1299721909",
                "LU1299722113",
                "LU1299722030"
            ],
            "title":"TARENO GLOBAL EQUITY FUND"
        },
        {
            "isin":[
                "LU0329630999",
                "LU0329630130"
            ],
            "title":"MIV GLOBAL MEDTECH FUND"
        }
    ]
}
'''
