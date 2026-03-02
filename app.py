from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Final Diagnostic: Deployment Success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
