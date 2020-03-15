from fastapi import FastAPI

app = FastAPI()

@app.post("/private/")
def read_private():
    return {"Hi": "This is private"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str=None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
