import logging
import traceback

from colorama import Fore
from fastapi import FastAPI, status, HTTPException, Depends, Response

from core import RefGen, get_ip, Usr

logging.basicConfig(
    format="%(levelname)s at %(asctime)s from %(name)s: %(message)s",
    datefmt="%m-%d %H:%M",
    level=logging.DEBUG,
    filename="logs.log",
    filemode="a"
)

api: FastAPI = FastAPI(
    title="User API",
    version="v1.0a",
    docs_url=None,
    redoc_url="/docs"
)
funcs: list[list[str]] = [["/usr/gen", "Generate an random username", "none"],
                          ["/usr/refgen", "Generate an username in base of references", "ref1: list[str], ref2: list[str]"],
                          ["/pass/gen", "Create an random password", "len: str"],
                          ["/", "Get this list of functions", "none"],
                          ["/docs", "Enter the docs", "none"]]

@api.get("/")
async def main(response: Response, client: str = Depends(get_ip)):
    return {"200": "success", "docs": funcs}


@api.get("/usr/gen")
async def gen(response: Response, client: str = Depends(get_ip)):
    try:
        logging.info(f"NEW_REQUEST: ip: {client}. Type: GET. Function: /usr/gen. Error: None.\nStatus: {response.status_code}")
        return {"200": "success", "username": Usr().generate()}
    except Exception as e:
        tberr = traceback.extract_tb(e.__traceback__)
        data = ""
        for frame in tberr:
            fname = frame.filename
            lineno = frame.lineno
            func = frame.name
            line = frame.line

            data = data + f"Error at line: {lineno} '{line}' in file {fname} and function {func}."

        print(Fore.RED + "ERROR: Details in log file" + Fore.RESET)
        logging.error(f"NEW_REQUEST: ip: {client}. Type: GET. Error:{data}.\nStatus: {response.status_code}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"500_ERR: An error happened: {e}"
        )

@api.get("/usr/refgen")
async def refgen(info: RefGen, response: Response, client: str = Depends(get_ip)):
    try:
        data = list(info.model_dump().values())

        logging.info(f"NEW_REQUEST: ip: {client}. Type: GET. Function: /usr/refgen. Error: None.\nStatus: {response.status_code}")
        return {"200": "success", "username": Usr(data).generate()}
    except Exception as e:
        tberr = traceback.extract_tb(e.__traceback__)
        data = ""
        for frame in tberr:
            fname = frame.filename
            lineno = frame.lineno
            func = frame.name
            line = frame.line

            data = data + f"Error at line: {lineno} '{line}' in file {fname} and function {func}."

        print(Fore.RED + "ERROR: Details in log file" + Fore.RESET)
        logging.error(f"NEW_REQUEST: ip: {client}. Type: GET. Error:{data}.\nStatus: {response.status_code}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"500_ERR: An error happened: {e}"
        )