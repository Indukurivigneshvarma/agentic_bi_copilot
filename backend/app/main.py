from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.data.loader import load_excel
from app.data.data_store import DATA_STORE
from app.agent.agent_controller import run_agent

app = FastAPI(title="Agentic BI Copilot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    df = load_excel(file)
    DATA_STORE["df"] = df
    return {
        "status": "success",
        "rows": len(df),
        "message": "Excel uploaded successfully"
    }

@app.post("/query")
async def query_data(payload: dict):
    query = payload.get("query")
    result = run_agent(query)
    return result
