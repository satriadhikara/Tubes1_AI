interface Iterations_history {
  iteration: number;
  obj_value: number;
}

export interface SearchResponse {
  message: string;
  initial_obj_value: number;
  final_obj_value: number;
  iterations: number;
  time: number;
  final_state: number[][][];
  initial_state: number[][][];
  iterations_history: Iterations_history[];
}

export interface ResultsProps {
  initial_state: number[][][];
  final_state: number[][][];
  initial_obj_value: number;
  final_obj_value: number;
  time: number;
  iterations: number;
  onBack: () => void;
  iterations_history: Iterations_history[];
}

export interface LandingProps {
  selectedAlgorithm: string;
  isPending: boolean;
  error: Error | null;
  onAlgorithmChange: (value: string) => void;
  onSubmit: (e: React.FormEvent) => void;
}

export interface MagicCubeProps {
  magic_cube: number[][][];
}
