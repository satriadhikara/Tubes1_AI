import React from "react";
import MagicCube1 from "./MagicCube";
import {
  Iterations_history,
  Iterations_history_sa,
  ResultsProps,
} from "../types";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  type ChartOptions,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const Results: React.FC<ResultsProps> = ({
  initial_state,
  final_state,
  initial_obj_value,
  final_obj_value,
  time,
  iterations,
  onBack,
  iterations_history,
  algorithm,
  frequency,
  restart_count,
  iterations_per_restart,
  population,
  max_fitness_history,
  avg_fitness_history,
}) => {
  const chartOptions: ChartOptions<"line"> = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "top",
        labels: { color: "white" },
      },
      tooltip: {
        backgroundColor: "rgba(0,0,0,0.8)",
      },
    },
    scales: {
      y: {
        title: {
          display: true,
          text: algorithm === "sa" ? "e^(-ΔE/T)" : "Objective Value",
          color: "white",
        },
        grid: { color: "rgba(255,255,255,0.1)" },
        ticks: { color: "white" },
      },
      x: {
        title: {
          display: true,
          text: "Iteration",
          color: "white",
        },
        grid: { color: "rgba(255,255,255,0.1)" },
        ticks: { color: "white" },
      },
    },
  };

  return (
    <div className="p-8 min-h-screen bg-gradient-to-r from-black to-slate-900 text-white">
      <div className="max-w-7xl mx-auto space-y-8">
        <button
          onClick={onBack}
          className="px-4 py-2 bg-gray-800 hover:bg-gray-700 text-white rounded-lg transition-colors duration-200 flex items-center gap-2"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fillRule="evenodd"
              d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"
              clipRule="evenodd"
            />
          </svg>
          Back
        </button>

        <div className="grid grid-cols-2 gap-12">
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <div className="h-3 w-3 rounded-full bg-blue-500"></div>
              <h2 className="text-xl font-semibold">Initial State</h2>
            </div>
            <div className="bg-gray-800/50 rounded-lg p-6">
              <MagicCube1 magic_cube={initial_state} />
            </div>
          </div>

          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <div className="h-3 w-3 rounded-full bg-green-500"></div>
              <h2 className="text-xl font-semibold">Final State</h2>
            </div>
            <div className="bg-gray-800/50 rounded-lg p-6">
              <MagicCube1 magic_cube={final_state} />
            </div>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-12 text-sm text-gray-400">
          <div>Initial State Objective Function: {initial_obj_value}</div>
          <div>Final State Objective Function: {final_obj_value}</div>
          <div>Computation Time: {time.toFixed(2)}s</div>
          <div>Number of Iterations: {iterations}</div>
          {frequency && <div>Frequency: {frequency}</div>}
          {restart_count && <div>Number of Restarts: {restart_count}</div>}
          {iterations_per_restart &&
            iterations_per_restart.map((iter, idx) => (
              <div key={idx}>
                Iterations in Restart {idx + 1}: {iter}
              </div>
            ))}
          {population && <div>Population Size: {population}</div>}
        </div>

        <div className="bg-gray-800/50 rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">
            Plot of{" "}
            {algorithm === "ga"
              ? "Fitness Values"
              : algorithm === "sa"
              ? "e^(-ΔE/T) "
              : "Objective Value "}
            vs Iteration
          </h2>
          <div className="h-[400px]">
            <div className="h-[400px]">
              {algorithm === "ga" ? (
                <Line
                  data={{
                    labels: Array.from(
                      { length: max_fitness_history!.length },
                      (_, i) => i + 1
                    ),
                    datasets: [
                      {
                        label: "Max Objective Function",
                        data: max_fitness_history,
                        borderColor: "#3b82f6",
                        backgroundColor: "rgba(59, 130, 246, 0.1)",
                        tension: 0.1,
                        fill: true,
                      },
                      {
                        label: "Average Objective Function",
                        data: avg_fitness_history,
                        borderColor: "#34d399",
                        backgroundColor: "rgba(52, 211, 153, 0.1)",
                        tension: 0.1,
                        fill: true,
                      },
                    ],
                  }}
                  options={chartOptions}
                />
              ) : (
                <Line
                  data={{
                    labels: iterations_history.map((h) => h.iteration),
                    datasets: [
                      {
                        label:
                          algorithm === "sa" ? "e^(-ΔE/T)" : "Objective Value",
                        data:
                          algorithm === "sa"
                            ? (
                                iterations_history as Iterations_history_sa[]
                              ).map((h) => h.eET)
                            : (iterations_history as Iterations_history[]).map(
                                (h) => h.obj_value
                              ),
                        borderColor: "#3b82f6",
                        backgroundColor: "rgba(59, 130, 246, 0.1)",
                        tension: 0.1,
                        fill: true,
                      },
                    ],
                  }}
                  options={chartOptions}
                />
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Results;
