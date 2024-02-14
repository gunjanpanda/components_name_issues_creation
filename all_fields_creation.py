import requests
import json
import pandas as pd

df = pd.read_excel('comp_cname.xlsx')

url = "https://gunjandemo.atlassian.net/rest/api/3/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
for index,row in df.iterrows():
    summary_text = row['Components'].split('-',1)[-1].strip()
    component_text = row['Components']
    description_text = "description for user: "+summary_text
    payload = json.dumps(
        {
            "fields": {
                "project":
                {
                    "key": "BUL"
                },
                "summary": summary_text + " - 750 UP7 IF04 Patch",
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {   
                            "type": "paragraph",
                            "content":[
                                {
                            "type": "text",
                            "text": description_text
                        }

                    ]
                }
                    ]
                },
                "issuetype": {
                    "name": "Task"
                },
                "priority": {
                    "name":"High"
                },
                
                "labels":["patch_750UP7IF04"],
                
                "components":[{"name": component_text}]
            }

        }
    )

    response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF01DfzwA9EZVRciO99vEymQXuoJ_OMArQQI8EVeNjhLq9BhD2RY6rfBwIqNCuI5kZVLkuyO_I8nEJ3pxr1El3Ke-9fWKYm_rd6zsL_2M1Lq-Y8m-r9yv6eAPyg7Iw6d0amEKPBxV8tfph7EldV-EnFwuIpUZ5Cew5Ci4Mk5aHihhI=9E3487FF"))
    print(response.text)