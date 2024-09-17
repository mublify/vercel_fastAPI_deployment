
from fastapi import FastAPI
import nest_asyncio
from transformers import pipeline

classifier = pipeline('sentiment-analysis', model = "cardiffnlp/twitter-roberta-base-sentiment-latest")

app = FastAPI()

@app.get('/')
async def home():

  return "Welcome to Our FastAPI Endpoints"


@app.get('/sentiment/{input}')
async def sentiment(input):
  results = classifier([input])
  return str(results)


@app.get('/ai')
async def ai():

  return "This is our second endpoint with FAST API"

@app.get('/table')
async def table():

  result = []
  for i in range(10):
    result.append(5*(i+1))

  return str(result)
