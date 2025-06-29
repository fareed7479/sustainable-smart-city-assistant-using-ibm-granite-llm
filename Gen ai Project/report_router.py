from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from report_generator import report_generator
import io

router = APIRouter()

@router.post("/report/generate")
async def generate_report(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    content = await file.read()
    try:
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")

    report = report_generator.generate_report(df)
    return {"report": report}
