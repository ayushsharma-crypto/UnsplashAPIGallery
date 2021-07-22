import uvicorn
from fastapi import FastAPI, Request
import requests
import json
from fastapi.templating import Jinja2Templates



client_id= 'lZMRQGbg6M4F1JBXyY--T60_RYOyM3XLCh_DzWGU6fQ'
url = 'https://api.unsplash.com/search/photos/'
query = 'Football'

unsplash_image = requests.get(url, params={'client_id': client_id ,'query':query, 'page':3, 'per_page':20}).json()

List_of_images =[]
unsplash_image = unsplash_image['results']

for i in unsplash_image:
    List_of_images.append(i['urls']['small'])

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request : Request):
    return  templates.TemplateResponse("index.html",{"request":request, "imgs":List_of_images})

if "__name__"=="__main__":
    uvicorn.run(app, host="127.0.0.10", port="8000")