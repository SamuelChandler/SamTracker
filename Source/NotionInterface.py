import requests
from datetime import datetime, timezone

NOTION_TOKEN = "secret_KDArq1ZKPiyQjU2DLxTUia1WxIgLVkeK81pbaVE9W9R"
NOTION_PAGE_ID_MAIN = "Main-b44b973ac289441a888528f47135a0ae"
DATABASE_ID = "ede5454f3b0e428ebc97ff6169b00db6?v=e56e816bac9a4b7f95a61ad0e738cce0&pvs=4"

headers = {
    "Authorization": "Bearer "+ NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_page():
    pass

def get_pages(num_Pages = None):
    
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"