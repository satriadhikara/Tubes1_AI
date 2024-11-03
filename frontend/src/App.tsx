import React, { useState } from "react";
import MagicCube from "./MagicCube";
import InputBar from "./InputBar";

const App: React.FC = () => {
    const [magicCube, setMagicCube] = useState<number[][][]>([]);
    const [algorithm, setAlgorithm] = useState<string>("default");

    const updateMagicCube = (parsedData: number[][][]) => {
        setMagicCube(parsedData);
    };

    const updateAlgorithm = (algorithm: string) => {
        setAlgorithm(algorithm);
    };

    return (
        <div className="flex flex-col">
            <div className="">
                <InputBar onParseInput={updateMagicCube} onAlgorithmChange={updateAlgorithm} />
            </div>
            <div className="">
                <MagicCube magicCube={magicCube} algorithm={algorithm} />
            </div>
        </div>
    );
};

export default App;
