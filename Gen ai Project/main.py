from fastapi import FastAPI
from chat_router import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

# Import other routers as stubs for now
from eco_tips_router import router as eco_tips_router
from feedback_router import router as feedback_router
from policy_search_router import router as policy_search_router
from kpi_forecast_router import router as kpi_forecast_router
from anomaly_detection_router import router as anomaly_detection_router
from report_router import router as report_router
from dashboard_router import router as dashboard_router

app = FastAPI(title="Sustainable Smart City Assistant API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(eco_tips_router)
app.include_router(feedback_router)
app.include_router(policy_search_router)
app.include_router(kpi_forecast_router)
app.include_router(anomaly_detection_router)
app.include_router(report_router)
app.include_router(dashboard_router)
