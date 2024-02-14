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

    response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF09bqoWkkUvq_92-XrsxsR55Hvd6SiekSTYJeae7LOX8fKKpdYX20YD87FOrT9g1DQuP7_k5-cmmaV_iXQXCpELUrKd_G8MWrRxjv33rLgl9JVXcalQvz4kB-h8I4SqpJ5cSI0cnL_Yg40JIz317jRFyXdImjD3vmVSoF4oTdoMOs=22E920B2"))
    print(response.text)