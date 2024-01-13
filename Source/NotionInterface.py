import requests
from Notion_Objects import *
from datetime import datetime, timezone

NOTION_TOKEN = "secret_KDArq1ZKPiyQjU2DLxTUia1WxIgLVkeK81pbaVE9W9R"
NOTION_PAGE_ID_MAIN = "Main-b44b973ac289441a888528f47135a0ae"
GROCERY_LIST_ID = "80ee8efd236e4196b49f62ebefc013ad"
PERSONAL_TASK_ID = "ede5454f3b0e428ebc97ff6169b00db6"

headers = {
    "Authorization": "Bearer "+ NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_page():
    print("Not Supported :)")
    pass

#function getting the pages from the static batabase ID 
def get_pages(ID ,num_Pages = None):
    
    url = f"https://api.notion.com/v1/databases/{ID}/query"

    payload = {"page_size": 100}
    response  = requests.post(url, json=payload, headers=headers)
    data = response.json()

    #writes data into a json file for testing and validation purposes
    import json
    with open('db.json','w',encoding='utf8') as f:
        json.dump(data["results"][0]["properties"], f,ensure_ascii=False, indent=4)

    #store and return results
    results = data["results"]
    return results

#Helper function that gets a list of grocery items from grocery list in Notion
def get_Grocery_List():

    grocery_list = []

    pages = get_pages(GROCERY_LIST_ID)
    for page in pages:

        #get page field that are needed
        props = page["properties"]
        name = props["Name"]["title"][0]["plain_text"] #Name of the grocery Item 
        catagory = props["Type"]["multi_select"][0]["name"] #only taking the first name of the type of item it is
        collected = props["Collected"]["checkbox"] #state showing if it has been collected
    
        #store in grocery list
        grocery_list.append(Grocery_Item(name,catagory,collected))

    #return Results
    return(grocery_list)

#Helper function that gets a list of grocery items from grocery list in Notion
def get_Personal_Task_List():
    personal_list = []
    pages = get_pages(PERSONAL_TASK_ID)
    for page in pages:

        #get page field that are needed
        props = page["properties"]
        name = props["Name"]["title"][0]["text"]["content"] #Name of the task
        catagory = props["Catagory"]["multi_select"][0]["name"] #only taking the first name of the type of task it is
        status = props["Status"]["status"]["name"] #state showing if it has been collected
        print(name,catagory,status)
        #store in grocery list
        personal_list.append(Personal_Task(name,catagory,status)) 

    #return Results
    return(personal_list)

PTL = get_Personal_Task_List()
for x in PTL:
    print(x.name)