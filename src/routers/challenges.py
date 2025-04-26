from fastapi import APIRouter
from src.services import challenges_service

router = APIRouter(
    prefix='/challenges',
    tags=['challenges']
)

@router.get('/solution-1')
async def get_challenge(n: int) -> int:
    return challenges_service.virus_propagation(n)