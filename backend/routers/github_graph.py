import requests
from fastapi import APIRouter, HTTPException
from config import settings
from utils import fetch_followers

github_router = APIRouter(prefix='/github', tags=['Github'])


@github_router.get("/{username}")
async def get_user_followers(username: str):
    """
    Get user followers with nested follower data.
    """
    try:
        # Gọi hàm fetch_followers để lấy dữ liệu followers
        data = fetch_followers(username)
        return data
    except ValueError as e:
        # Xử lý lỗi logic, ví dụ: user không tồn tại
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        # Xử lý các lỗi khác
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@github_router.get("/hello/{name}")
async def say_hello(name: str):

    return {"message": f"Hello {name}",
            "Age": f"How old are you?",
            "Occupation": f"What do you do?",
            "Profession": f"What major are you in?"
            }
@github_router.get("/information/{name}")
async def get_information(name: str):
    token = settings.GITHUB_API_TOKEN
    headers = {
      "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{name}"

    # Делаем запрос и получаем ответ
    response = requests.get(url, headers=headers)

    if response.status_code == 200:  # Проверка кода ответа
        return response.json()
    elif response.status_code == 404:
        return {"status": 401, "message": "Ай-ай-ай, неверный токен авторизации!"}  # Отправляем своё сообщение и код ошибки
    else:
        return response.json()
