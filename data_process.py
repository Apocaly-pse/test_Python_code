import json

import pandas as pd

pd.set_option('expand_frame_repr', False)


def json2csv(jsonFile):
    with open(jsonFile, 'r') as f:
        data = json.loads(f.read())
    ret1 = data['component'][0]['caseList']
    return ret1


ret = json2csv("result.json")
tmp_df = pd.DataFrame(ret)
df1 = pd.DataFrame(tmp_df[["area", "confirmedRelative", "curConfirm", "confirmed", "crued", "died"]].values,
                   columns=["地区", "新增", "现有", "累计", "治愈", "死亡"])
df1.to_csv("result-1.csv")
print(df1)
