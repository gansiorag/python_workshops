from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import json

async def create_user(request):
    # 1. Ручное извлечение тела запроса
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return JSONResponse({"error": "Invalid JSON"}, status_code=400)
    
    # 2. Ручная валидация
    name = data.get("name")
    age = data.get("age")
    
    if not name or not isinstance(age, int) or age < 18:
        return JSONResponse({"error": "Invalid data or age < 18"}, status_code=400)
    
    return JSONResponse({"status": "ok", "user": name})

app = Starlette(routes=[
    Route("/user", create_user, methods=["POST"]),
])