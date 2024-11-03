import React, { useState } from "react";

interface InputBarProps {
    onParseInput: (parsedData: number[][][]) => void;
    onAlgorithmChange: (algorithm: string) => void;
}

const InputBar: React.FC<InputBarProps> = ({ onParseInput, onAlgorithmChange }) => {
    const [inputText, setInputText] = useState("");
    const [algorithm, setAlgorithm] = useState("default");

    const handleParseInput = () => {
        const sections = inputText.trim().split(/\n\s*\n/);
        const parsedData = sections.map((section) =>
            section.split("\n").map((line) =>
                line.trim().split(/\s+/).map(Number)
            )
        );

        onParseInput(parsedData);
    };

    const handleGenerateRandom = () => {
        const randomData: number[][][] = [];
        const usedNumbers = new Set<number>();
        const getRandomNumber = () => {
            let num;
            do {
                num = Math.floor(Math.random() * 125) + 1;
            } while (usedNumbers.has(num));
            usedNumbers.add(num);
            return num;
        };

        for (let x = 0; x < 5; x++) {
            const plane = [];
            for (let y = 0; y < 5; y++) {
                const row = Array.from({ length: 5 }, getRandomNumber);
                plane.push(row);
            }
            randomData.push(plane);
        }

        onParseInput(randomData);
    };

    const handleAlgorithmChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setAlgorithm(event.target.value);
        onAlgorithmChange(event.target.value);
    };

    return (
        <div className="p-6 bg-gray-100 w-screen flex flex-row justify-center gap-52">
            <div>
                <h1 className="text-2xl font-bold mb-4">Magic Cube Input</h1>
                <textarea
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    placeholder="Enter the magic cube data here..."
                    rows={10}
                    className="w-full max-w-md p-2 border border-gray-300 rounded mb-4"
                ></textarea>
                <button
                    onClick={handleParseInput}
                    className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mb-2"
                >
                    Parse and Append Input
                </button>
            </div>

            {/* Algorithm selection radio buttons */}
            <div className="mb-4 flex flex-col gap-10">
                <div>
                    <label className="text-2xl font-bold mb-4 block">Generate Random Input</label>
                    <button
                        onClick={handleGenerateRandom}
                        className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 mb-4"
                    >
                        Generate Random
                    </button>                    
                </div>
                <div>
                    <label className="text-2xl font-bold mb-4 block">Choose Algorithm</label>
                    <div className="flex flex-col gap-4">
                        <label className="flex items-center">
                            <input
                                type="radio"
                                name="algorithm"
                                value="Hill-Climbing"
                                checked={algorithm === "Hill-Climbing"}
                                onChange={handleAlgorithmChange}
                                className="mr-2"
                            />
                            Hill-Climbing
                        </label>
                        <label className="flex items-center">
                            <input
                                type="radio"
                                name="algorithm"
                                value="Simulated Annealing"
                                checked={algorithm === "Simulated Annealing"}
                                onChange={handleAlgorithmChange}
                                className="mr-2"
                            />
                            Simulated Annealing
                        </label>
                        <label className="flex items-center">
                            <input
                                type="radio"
                                name="algorithm"
                                value="Genetic Algorithm"
                                checked={algorithm === "Genetic Algorithm"}
                                onChange={handleAlgorithmChange}
                                className="mr-2"
                            />
                            Genetic Algorithm
                        </label>
                    </div>

                </div>
            </div>
        </div>
    );
};

export default InputBar;
