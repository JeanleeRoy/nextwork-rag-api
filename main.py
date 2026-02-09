from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

'''
In this step, you're going to:

Write content in your knowledge base
Create a script that prepares your content for AI search
Run the script to make your content searchable
✍️ What are we doing in this step?

Complete, give short answers

In this step, I'm creating a knowledge base with relevant information and preparing it for AI search.
A knowledge base is a centralized repository of information that can be easily accessed and searched.
I need it because it allows me to organize and store information in a way that can be efficiently retrieved by AI models, improving the accuracy and relevance of search results.
'''