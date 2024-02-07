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
    summary_text = row['Customer_name']
    component_text = row['Components']
    description_text = "description for user: "+summary_text
    payload = json.dumps(
        {
            "fields": {
                "project":
                {
                    "key": "BUL"
                },
                "summary": summary_text + "750 UP7 IF04 Patch",
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

    response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF0f-zAUKOjgHqRXOHnjJStKfjsl5HDV4dqbOw8qaN5VDQXPsxPjIMItmjLYI8_mr37P9AWH3UO5lB4erucUz_WdsMpXypZ7fO9jlAc_N89KoslAL3yXER-z4boRPsmawjEl-5SVsaRz-tZcyD6OSHmGyTapTz1RX3Bd9XeVSZ3TMQ=01028EBD"))
    print(response.text)