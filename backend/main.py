from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.gzip import GZipMiddleware
from algorithms.index import solve_cube

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)

HELLO_RESPONSE = {"Hello": "World"}


class SearchRequest(BaseModel):
    algorithm: str
    initial_state: list[list[list[int]]]


class SearchResponse(BaseModel):
    message: str
    total_deviation: int
    iterations: int
    time: float
    final_state: list[list[list[int]]]


class SearchResponseGA(SearchResponse):
    population: list[list[list[int]]]


class SearchResponseSA(SearchResponse):
    frequency: int


@app.get("/")
def read_root():
    return HELLO_RESPONSE


@app.get("/search")
def search(req: SearchRequest) -> SearchResponse | SearchResponseGA | SearchResponseSA:
    message, total_deviation, iterations, time, final_state, frequency, population = (
        solve_cube(
            req.initial_state,
            req.algorithm,
        )
    )

    if req.algorithm == "ga":
        return SearchResponseGA(
            message=message,
            total_deviation=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            population=population,
        )
    elif req.algorithm == "sa":
        return SearchResponseSA(
            message=message,
            total_deviation=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            frequency=frequency,
        )
    elif req.algorithm == "hc":
        return SearchResponse(
            message=message,
            total_deviation=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
        )
