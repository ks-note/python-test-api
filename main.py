import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import JSONResponse
​
app = FastAPI()
​
@app.get("/api/users")
async def list():
    return JSONResponse(
        status_code=200,
        content={"id": "100001", "name": "zhangsan"},
    )
​
@app.get("/api/users/5xx")
async def error():
    return JSONResponse(status_code=500)
​
@app.get("/api/users/host-name")
async def get_container_name():
    try:
        with open("/etc/hostname", "r") as f:
            container_name = f.read().strip()
        return {"hostname": container_name}
    except Exception as e:
        return {"error": str(e)}
​
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80) 
