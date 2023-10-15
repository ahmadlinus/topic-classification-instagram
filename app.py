from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import uvicorn
from model import TopicClassifier
from pydantic import BaseModel

app = FastAPI()

# model-sp
topics = ["Sport", "Art", "Politics", "Food"]
topic_model = TopicClassifier(topics)


# data schema for inputs
class TopicClassifierInput(BaseModel):
    text: str


@app.get("/")
async def entry_point():
    return Response(content="Hello World! Welcome to Topic Classification!")


@app.post("/topics")
async def get_topic_distribution(item: TopicClassifierInput):
    # receive input text
    text = item.text

    # make predictions
    predictions = topic_model.predict(text)
    
    # format output
    output = {topics[x]: predictions[x] for x in list(range(len(topics)))}

    return JSONResponse(content=output)


if __name__ == '__main__':
    NUM_WORKERS = 3

    # run UVICORN server
    uvicorn.run("app:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=False, 
        loop="asyncio", 
        workers=NUM_WORKERS, 
        log_config="log.ini"
    )
