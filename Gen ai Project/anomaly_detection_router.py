from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from sklearn.ensemble import IsolationForest
import io

router = APIRouter()

@router.post("/anomaly/detect")
async def detect_anomalies(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    content = await file.read()
    try:
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")

    if df.empty:
        raise HTTPException(status_code=400, detail="CSV file is empty.")

    model = IsolationForest(contamination=0.05)
    preds = model.fit_predict(df.select_dtypes(include=['float64', 'int64']))
    anomalies = df[preds == -1]

    return {"anomalies": anomalies.to_dict(orient="records")}
