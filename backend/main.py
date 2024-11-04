from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from algorithms.index import solve_cube
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

HELLO_RESPONSE = {"Hello": "World"}


class SearchRequest(BaseModel):
    algorithm: str


class IterationHistoryHC(BaseModel):
    iteration: int
    obj_value: int


class IterationHistorySA(BaseModel):
    iteration: int
    eET: float


class SearchResponse(BaseModel):
    message: str
    initial_obj_value: int
    final_obj_value: int
    iterations: int
    time: float
    initial_state: list[list[list[int]]]
    final_state: list[list[list[int]]]


class SearchResponseHC(SearchResponse):
    iterations_history: list[IterationHistoryHC]


class SearchResponseGA(SearchResponse):
    population: list[list[list[int]]]


class SearchResponseSA(SearchResponse):
    frequency: int
    iterations_history: list[IterationHistorySA]


class SearchResponseHCRR(SearchResponseHC):
    restart_count: int
    iterations_per_restart: list[int]


@app.get("/")
def read_root():
    time.sleep(10)  # Debugging purpose
    return HELLO_RESPONSE


@app.post("/search")
def search(
    req: SearchRequest,
) -> SearchResponseHC | SearchResponseGA | SearchResponseSA | SearchResponseHCRR:
    (
        message,
        total_deviation,
        iterations,
        time,
        final_state,
        frequency,
        population,
        initial_state,
        initial_obj_value,
        iterations_history,
        restart_count,
        iterations_per_restart,
    ) = solve_cube(
        req.algorithm,
    )

    if req.algorithm == "hc":
        return SearchResponseHC(
            message=message,
            initial_obj_value=initial_obj_value,
            final_obj_value=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            initial_state=initial_state,
            iterations_history=iterations_history,
        )
    elif req.algorithm == "hc-stochastic":
        return SearchResponseHC(
            message=message,
            initial_obj_value=initial_obj_value,
            final_obj_value=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            initial_state=initial_state,
            iterations_history=iterations_history,
        )
    elif req.algorithm == "hc-sideways":
        return SearchResponseHC(
            message=message,
            initial_obj_value=initial_obj_value,
            final_obj_value=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            initial_state=initial_state,
            iterations_history=iterations_history,
        )
    elif req.algorithm == "hc-random-restart":
        return SearchResponseHCRR(
            message=message,
            initial_obj_value=initial_obj_value,
            final_obj_value=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            initial_state=initial_state,
            iterations_history=iterations_history,
            restart_count=restart_count,
            iterations_per_restart=iterations_per_restart,
        )
    elif req.algorithm == "sa":
        return SearchResponseSA(
            message=message,
            initial_obj_value=initial_obj_value,
            final_obj_value=total_deviation,
            iterations=iterations,
            time=time,
            final_state=final_state,
            frequency=frequency,
            initial_state=initial_state,
            iterations_history=iterations_history,
        )
