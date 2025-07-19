from fastapi import APIRouter

router = APIRouter()

@router.get("/auth-check")
def check():
    return {"msg": "Auth route working"}
