import React from "react";
import { Button } from "@nextui-org/button";
import { Select, SelectItem } from "@nextui-org/react";
import { LandingProps } from "../types";

const Landing: React.FC<LandingProps> = ({
  selectedAlgorithm,
  isPending,
  error,
  onAlgorithmChange,
  onSubmit,
}) => {
  return (
    <div className="h-screen flex flex-col justify-center items-center font-poppins bg-gradient-to-r from-black to-slate-900 text-white">
      <h1 className="text-3xl font-semibold mb-10">
        (Perfect) Magic Cube Problems With Local Search
      </h1>
      <img src="../image.png" className="w-32 h-32 mb-8" alt="" />
      <div className="w-96 flex">
        <form onSubmit={onSubmit} className="w-full flex flex-col items-center">
          <Select
            className="mb-4 w-full"
            size="sm"
            label="Select an algorithm"
            required
            value={selectedAlgorithm}
            onChange={(e) => onAlgorithmChange(e.target.value)}
            isDisabled={isPending}
          >
            <SelectItem key="hc" value="hc">
              HC Steepest Ascent
            </SelectItem>
            <SelectItem key="hc_r" value="hc_r">
              HC Random Restart
            </SelectItem>
            <SelectItem key="hc-sideways" value="hc-sideways">
              HC Sideways Move
            </SelectItem>
            <SelectItem key="hc_s_r" value="hc_s_r">
              HC Stochastic
            </SelectItem>
            <SelectItem key="sa" value="sa">
              Simulated Annealing
            </SelectItem>
            <SelectItem key="ga" value="ga">
              Genetic Algorithm
            </SelectItem>
          </Select>

          <Button
            type="submit"
            className="w-full"
            isLoading={isPending}
            isDisabled={!selectedAlgorithm || isPending}
          >
            {isPending ? "Searching..." : "Search!"}
          </Button>

          {error && (
            <p className="text-red-500 mt-2">
              {error instanceof Error ? error.message : "An error occurred"}
            </p>
          )}
        </form>
      </div>
    </div>
  );
};

export default Landing;
