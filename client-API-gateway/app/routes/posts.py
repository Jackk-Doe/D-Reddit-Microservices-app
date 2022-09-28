from fastapi import APIRouter, HTTPException, Depends, Body, Request
from fastapi.security import OAuth2PasswordBearer
from httpx import Response
import httpx

import load_envs as _envs

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/')
async def testRoute():
    return {"TEST": "Hello from APIGateway : POST route"}


@router.get('/test')
async def testConnect():
    try:
        res = httpx.get(f"{_envs.POST_SERVICES_URL}")
        return res.json()
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))


@router.get('/rooms')
async def getRooms(*, recommend = False, request: Request):
    try:
        res: Response = None

        if recommend:
            _bearer_and_token = request.headers.get('authorization')
            _headers = {'Authorization': _bearer_and_token}
            res = httpx.get(f"{_envs.POST_SERVICES_URL}/posts/rooms?recommend={recommend}", headers=_headers)
        else:
            res = httpx.get(f"{_envs.POST_SERVICES_URL}/posts/rooms")

        _res = res.json()
        if res.status_code != 200:
            #! Error : Found error from calling service
            return {'status_code': res.status_code, 'detail': _res['detail']}
        return _res
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))


@router.get('/rooms/{room_id}')
async def getById(room_id: int, request: Request):
    try:
        _bearer_and_token = request.headers.get('authorization')
        if _bearer_and_token is not None:
            _headers = {'Authorization': _bearer_and_token}
            res = httpx.get(f"{_envs.POST_SERVICES_URL}/posts/rooms/{room_id}", headers=_headers)
        else:
            res = httpx.get(f"{_envs.POST_SERVICES_URL}/posts/rooms/{room_id}")
            
        _res = res.json()
        if res.status_code != 200:
            return {'status_code': res.status_code, 'detail': _res['detail']}
        return _res
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))


@router.post('/rooms')
async def createRoom(payload: dict = Body(), token: str = Depends(oauth2_scheme)):
    try:
        _headers = {'Authorization': 'Bearer ' + token}
        res = httpx.post(f"{_envs.POST_SERVICES_URL}/posts/rooms", json=payload, headers=_headers)
        _res = res.json()
        if res.status_code != 200:
            return {'status_code': res.status_code, 'detail': _res['detail']}
        return _res
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))


@router.patch('/rooms/{room_id}')
async def updateRoom(room_id: int, payload: dict = Body(), token: str = Depends(oauth2_scheme)):
    try:
        _headers = {'Authorization': 'Bearer ' + token}
        res = httpx.patch(f"{_envs.POST_SERVICES_URL}/posts/rooms/{room_id}", json=payload, headers=_headers)
        _res = res.json()
        if res.status_code != 200:
            return {'status_code': res.status_code, 'detail': _res['detail']}
        return _res
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))


@router.delete('/room/{room_id}')
async def deleteRoom(room_id: int, token: str = Depends(oauth2_scheme)):
    try:
        _headers = {'Authorization': 'Bearer ' + token}
        res = httpx.delete(f"{_envs.POST_SERVICES_URL}/posts/rooms/{room_id}", headers=_headers)
        _res = res.json()
        if res.status_code != 200:
            return {'status_code': res.status_code, 'detail': _res['detail']}
        return _res
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))


@router.post('/rooms/{room_id}/add-message')
async def addMessage(room_id: int, payload: dict = Body(), token: str = Depends(oauth2_scheme)):
    try:
        _headers = {'Authorization': 'Bearer ' + token}
        res = httpx.post(f"{_envs.POST_SERVICES_URL}/posts/rooms/{room_id}/add-message", json=payload, headers=_headers)
        _res = res.json()
        if res.status_code != 200:
            return {'status_code': res.status_code, 'detail': _res['detail']}
        return _res
    except Exception as _error:
        return HTTPException(status_code=500, detail=str(_error))