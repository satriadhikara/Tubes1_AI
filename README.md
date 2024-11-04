# Solution Search for Diagonal Magic Cube with Local Search

This repository contains a program to find solutions for a **Diagonal Magic Cube** using various _Local Search_ methods. Built with _React.js_ and _TypeScript_, this interactive application allows users to experiment with different algorithms to achieve a solution. Implemented algorithms include _Steepest Ascent Hill Climbing_, _Simulated Annealing_, _Random Restart Hill Climbing_, _Stochastic Hill Climbing_, and _Genetic Algorithm_, which are used to find optimal or near-optimal configurations for the diagonal magic cube.

## Table of Contents

- [Description](#description)
- [Setup Instructions](#setup-instructions)
- [Running the Program](#running-the-program)
- [Contributors](#contributors)

## Description

A Diagonal Magic Cube is a variant of a magic cube in which every diagonal has the same sum. This program focuses on finding a solution to the diagonal magic cube problem using _Local Search_ methods, which efficiently explore the large solution space to find configurations that meet the cube's requirements.

## Setup Instructions

1. **Ensure** that you have [bun](https://bun.sh/) and [uv](https://docs.astral.sh/uv/) installed on your system.
2. Clone this repository to your local directory:
   ```bash
   git clone https://github.com/satriadhikara/Tubes1_AI.git
   ```

## Running the Program

### Running the Frontend

1. Change directory to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install the necessary dependencies:
   ```bash
   bun install
   ```
3. Run the frontend application:
   ```bash
   bun dev
   ```

### Running the Backend

1. Change directory to the backend folder:
   ```bash
   cd backend
   ```
2. Install the necessary dependencies:
   ```bash
   uv sync
   ```
3. Run the backend application:
   ```bash
   uv run fastapi run
   ```

## Contributors

| NIM      | Role                                                                  |
| -------- | --------------------------------------------------------------------- |
| 13522125 | Simulated Annealing, Steepest Ascent Hill-climbing Algorithm, API, UI |
| 13522128 | Genetic Algorithm, Stochastic Algorithm, Document                     |
| 13522148 | Random Restart Hill-climbing, Cube Visualization, Document            |
| 13522162 | Sideways Move Hill-climbing, Cube Visualization, Document             |
