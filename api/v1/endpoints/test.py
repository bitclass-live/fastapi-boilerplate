from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/", summary="this is a summary of this call")
async def read_base():
    return [{"username": "Hello"}, {"username": "World"}]
