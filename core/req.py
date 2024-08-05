from fastapi import Request, Response


def get_ip(request: Request) -> str:
    return request.client.host