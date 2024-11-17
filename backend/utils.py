import requests
from config import settings

def fetch_followers(username: str, depth: int = 1, max_depth: int = 2):
    """
    Fetch followers recursively up to max_depth.
    """
    if depth > max_depth:
        return []

    token = settings.GITHUB_API_TOKEN
    if not token:
        raise ValueError("GitHub API token is missing in the configuration.")

    headers = {
        "Authorization": f"token {token}"
    }
    url = f"https://api.github.com/users/{username}/followers"

    response = requests.get(url, headers=headers, proxies={"http": None, "https": None})
    if response.status_code == 200:
        followers = response.json()
        followers_data = []
        for follower in followers:
            follower_data = {
                "login": follower["login"],
                "avatar_url": follower["avatar_url"],
                "size": calculate_size(len(followers)),  # Tính kích thước biểu tượng dựa trên số lượng followers
                "followers": fetch_followers(follower["login"], depth + 1, max_depth)
            }
            followers_data.append(follower_data)
        return followers_data
    elif response.status_code == 404:
        raise ValueError(f"User '{username}' not found on GitHub.")
    elif response.status_code == 401:
        raise ValueError("Invalid GitHub API token.")
    else:
        raise ValueError(f"GitHub API error: {response.status_code} - {response.text}")

def calculate_size(follower_count: int) -> int:
    """
    Calculate avatar size based on follower count.
    """
    return max(16, min(128, follower_count * 4))
