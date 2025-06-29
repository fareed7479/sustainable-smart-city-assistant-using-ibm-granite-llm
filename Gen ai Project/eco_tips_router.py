from fastapi import APIRouter

router = APIRouter()

@router.get("/eco-tips")
async def get_eco_tips(keyword: str):
    return {"tips": [f"Tip {i+1} for {keyword}" for i in range(5)]}
