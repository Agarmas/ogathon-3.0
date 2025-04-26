from itertools import permutations
from fastapi import APIRouter, Depends
from src.services import challenges_service
from src.models.challenges_models import QueryN, RecycleMatrix

router = APIRouter(
    prefix='/challenges',
    tags=['challenges'],
)

@router.get('/solution-1')
async def virus_propagation(params: QueryN = Depends()) -> str:
    return str(challenges_service.virus_propagation(params.n))

@router.get('/solution-2')
async def count_end89(params: QueryN = Depends()) -> str:
    return str(challenges_service.count_end89(params.n))

@router.post('/solution-3')
async def recycling(matrix: RecycleMatrix) -> str:
    data = matrix.root

    return str(challenges_service.recycling(data))