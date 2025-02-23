from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/test")
async def get_u():
    return {"message": "ghello"}
