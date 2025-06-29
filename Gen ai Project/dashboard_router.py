from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/summary")
async def get_dashboard_summary(city: str = "default"):
    # Placeholder: return KPI summary cards and city info
    return {
        "city": city,
        "kpi_summary": {
            "water_usage": 1234,
            "energy_usage": 5678,
            "carbon_emissions": 910
        }
    }
