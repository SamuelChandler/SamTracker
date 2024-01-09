import requests
from datetime import datetime, timezone

NOTION_TOKEN = "secret_KDArq1ZKPiyQjU2DLxTUia1WxIgLVkeK81pbaVE9W9R"
NOTION_PAGE_ID_MAIN = "Main-b44b973ac289441a888528f47135a0ae"
DATABASE_ID = "ede5454f3b0e428ebc97ff6169b00db6"

headers = {
    "Authorization": "Bearer "+ NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_page():
    pass

def get_pages(num_Pages = None):
    
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response  = requests.post(url, json=payload, headers=headers)
    data = response.json()

    import json
    with open('db.json','w',encoding='utf8') as f:
        json.dump(data, f,ensure_ascii=False, indent=4)

    results = data["results"]
    return results

pages = get_pages()
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    url = props["URL"]["title"][0]["text"]["content"]
    title = props["Title"]["rich_text"][0]["text"]["content"]
    published = props["Published"]["date"]["start"]
    published = datetime.fromisoformat(published)
    print(url,title,published)