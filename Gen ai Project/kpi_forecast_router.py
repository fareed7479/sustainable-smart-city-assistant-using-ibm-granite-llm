from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from sklearn.linear_model import LinearRegression
import io

router = APIRouter()

@router.post("/kpi/forecast")
async def forecast_kpi(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    content = await file.read()
    try:
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")

    if df.shape[1] < 2:
        raise HTTPException(status_code=400, detail="CSV must have at least two columns (time and KPI).")

    # Assume first column is time/index, second column is KPI value
    X = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1].values

    model = LinearRegression()
    model.fit(X, y)
    next_x = [[X[-1][0] + 1]]
    forecast = model.predict(next_x)[0]

    return {"forecast": forecast}
