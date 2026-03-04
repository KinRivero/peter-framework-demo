"""FastAPI REST API for calculator operations."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.calculator import add, subtract, multiply, divide, power

app = FastAPI(
    title="Calculator API",
    description="A simple calculator API demonstrating the PETER framework",
    version="1.0.0",
)


class OperationRequest(BaseModel):
    """Request body for binary operations."""
    a: float
    b: float


class ResultResponse(BaseModel):
    """Response body with calculation result."""
    result: float
    operation: str


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


@app.post("/add", response_model=ResultResponse)
def api_add(req: OperationRequest):
    """Add two numbers."""
    return ResultResponse(result=add(req.a, req.b), operation="add")


@app.post("/subtract", response_model=ResultResponse)
def api_subtract(req: OperationRequest):
    """Subtract b from a."""
    return ResultResponse(result=subtract(req.a, req.b), operation="subtract")


@app.post("/multiply", response_model=ResultResponse)
def api_multiply(req: OperationRequest):
    """Multiply two numbers."""
    return ResultResponse(result=multiply(req.a, req.b), operation="multiply")


@app.post("/divide", response_model=ResultResponse)
def api_divide(req: OperationRequest):
    """Divide a by b."""
    try:
        return ResultResponse(result=divide(req.a, req.b), operation="divide")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/power", response_model=ResultResponse)
def api_power(req: OperationRequest):
    """Raise a to the power of b."""
    try:
        return ResultResponse(result=power(req.a, req.b), operation="power")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
