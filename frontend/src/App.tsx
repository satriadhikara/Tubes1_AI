import React, { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import Results from "./components/Result";
import Landing from "./components/Landing";
import { SearchResponse } from "./types";

const App = () => {
  const [selectedAlgorithm, setSelectedAlgorithm] = useState("");

  const { mutate, isPending, data, error } = useMutation<SearchResponse>({
    mutationFn: async () => {
      const response = await fetch(`http://localhost:8000/search`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          algorithm: selectedAlgorithm,
        }),
      });
      if (!response.ok) {
        throw new Error("Network response failed");
      }
      return response.json();
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    mutate();
  };

  if (data) {
    console.log(data);
    return (
      <Results
        initial_state={data.initial_state}
        final_state={data.final_state}
        initial_obj_value={data.initial_obj_value}
        final_obj_value={data.final_obj_value}
        time={data.time}
        iterations={data.iterations}
        onBack={() => window.location.reload()}
        iterations_history={data.iterations_history}
        algorithm={selectedAlgorithm}
        frequency={data.frequency}
      />
    );
  }

  return (
    <Landing
      selectedAlgorithm={selectedAlgorithm}
      isPending={isPending}
      error={error}
      onAlgorithmChange={setSelectedAlgorithm}
      onSubmit={handleSubmit}
    />
  );
};

export default App;
