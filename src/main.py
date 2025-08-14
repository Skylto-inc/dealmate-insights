from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Analytics Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "analytics-service", "features": ["data_analysis", "reporting"]}

@app.get("/analytics/dashboard")
async def get_dashboard():
    return {
        "metrics": {
            "total_users": 10000,
            "total_deals": 5000,
            "savings_generated": 250000
        },
        "service": "analytics-service"
    }

@app.get("/analytics/user/{user_id}")
async def get_user_analytics(user_id: str):
    return {
        "user_id": user_id,
        "total_savings": 1250.50,
        "deals_used": 25,
        "service": "analytics-service"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
