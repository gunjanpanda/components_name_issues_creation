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

    response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF0HrJlPBM0H_kd8gLkNffl_S59uHu-fe17arf28_Y0grU_DbyZnVcYWpNG84zKgXJUaTpB4LGTK02flX9nRONlLvPsYv4Dsn-TjqGjcCTblVk10T4GGPhocf8vJ-PVeBXV8C6QbLZ0oSAp0FtiDHarOFORX032XKq9YrvwSagpaWE=B47F5D88"))
    print(response.text)