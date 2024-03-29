import requests
from Notion_Objects import *
from datetime import datetime, timezone

NOTION_TOKEN = "secret_KDArq1ZKPiyQjU2DLxTUia1WxIgLVkeK81pbaVE9W9R"
NOTION_PAGE_ID_MAIN = "Main-b44b973ac289441a888528f47135a0ae"
GROCERY_LIST_ID = "80ee8efd236e4196b49f62ebefc013ad"
PERSONAL_TASK_ID = "ede5454f3b0e428ebc97ff6169b00db6"
SCHOOL_TASK_ID = "76a6332594b54ac196c86ce41e4cd9ec"

headers = {
    "Authorization": "Bearer "+ NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_page():
    print("Not Supported :)")
    pass

#function getting the pages from the static batabase ID 
def get_pages(database_ID: str ,num_Pages = None):
    
    url = f"https://api.notion.com/v1/databases/{database_ID}/query"

    getAll = num_Pages is None
    page_size = 100 if getAll else num_Pages

    payload = {"page_size": page_size}
    response  = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 200:
        print("Error with get_pages: " + response.status_code)
    else:
        print("get sucessful")
    
    
    data = response.json()

    #writes data into a json file for testing and validation purposes
    import json
    with open('db.json','w',encoding='utf8') as f:
        json.dump(data["results"], f,ensure_ascii=False, indent=4)

    #store results
    results = data["results"]

    #move to next 100 pages extending onto the previos results
    while data["has_more"] and getAll:
        payload = {"page_size":page_size, "start_cursor": data["next_cursor"]}
        response  = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results

#Helper function that gets a list of grocery items from grocery list in Notion
def get_Grocery_List(page_number = None):

    grocery_list = []

    pages = get_pages(GROCERY_LIST_ID,page_number)
    for page in pages:

        #get page field that are needed
        props = page["properties"]
        name = props["Name"]["title"][0]["plain_text"] #Name of the grocery Item 
        catagory = props["Type"]["select"]["name"] #only taking the first name of the type of item it is
        collected = props["Collected"]["checkbox"] #state showing if it has been collected
    
        #store in grocery list
        grocery_list.append(Grocery_Item(name,catagory,collected))

    #return Results
    return(grocery_list)

#Helper function that gets a list of personal task items from personal Task list in Notion
def get_Personal_Task_List(page_number = None):

    personal_list = []

    pages = get_pages(PERSONAL_TASK_ID,page_number)
    for page in pages:

        #get page field that are needed
        props = page["properties"]
        name = props["Name"]["title"][0]["text"]["content"] #Name of the task
        catagory = props["Catagory"]["multi_select"][0]["name"] #only taking the first name of the type of task it is
        status = props["Status"]["status"]["name"] #state showing if it has been completed
        
        #store in grocery list
        personal_list.append(Personal_Task(name,catagory,status)) 

    #return Results
    return(personal_list)

#Helper function that gets a list of school task items from school Task list in Notion
def get_School_Task_List(page_number = None):
    school_list = []
    pages = get_pages(SCHOOL_TASK_ID, page_number)
    for page in pages:

        #get page field that are needed
        props = page["properties"]
        name = props["Name"]["title"][0]["text"]["content"] #Name of the task
        course = props["Class"]["select"]["name"] #the tasks related class
        status = props["Status"]["status"]["name"] #state showing if it has completed
        type = props["Type of work"]["multi_select"][0]["name"]#only taking the first name of the type of task it is
        
        #store in grocery list
        school_list.append(School_Task(name,course,status,type)) 

    #return Results
    return(school_list)

#Adds a grocery item to the grocery item database in Notion
def Add_Grocery_Item(item: Grocery_Item):
    data = item.to_Data(GROCERY_LIST_ID)
    
    url = f"https://api.notion.com/v1/pages"

    res = requests.post(url, json=data, headers=headers)

    if(res.status_code != 200):
        print("POST Error: " + res.status_code)
    else:
        print("successful POST")
    return res

#Adds a personal task to notion database
def Add_Personal_Task(item: Personal_Task):
    data = item.to_Data(PERSONAL_TASK_ID)
    
    url = f"https://api.notion.com/v1/pages"

    res = requests.post(url, json=data, headers=headers)

    if(res.status_code != 200):
        print("POST Error: " + res.status_code)
    else:
        print("successful POST")
    return res

#Adds a school task to its notion Database
def Add_School_Task(item: School_Task):
    data = item.to_Data(SCHOOL_TASK_ID)
    
    url = f"https://api.notion.com/v1/pages"

    res = requests.post(url, json=data, headers=headers)

    if(res.status_code != 200):
        print("POST Error: " + res.status_code)
    else:
        print("successful POST")
    return res

