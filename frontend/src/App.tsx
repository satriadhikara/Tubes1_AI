import React from "react";
import MagicCube from "./MagicCube";
<<<<<<< HEAD
<<<<<<< HEAD
import MagicCube1 from "./MagicCube1";
import Result from "./Result";
import './App.css';

const App: React.FC = () => {
    return (
        <div className=" p-6">
            <Result />
            <div className='flex flex-row gap-6'>
                <MagicCube />
                <MagicCube1 />
            </div>
        </div>
        

    );
};

=======
=======
import MagicCube1 from "./MagicCube1";
import Result from "./Result";
import './App.css';
>>>>>>> cb296d4 (feat : result display UI)

const App: React.FC = () => {
    return (
        <div className=" p-6">
            <Result />
            <div className='flex flex-row gap-6'>
                <MagicCube />
                <MagicCube1 />
            </div>
        </div>
        

    );
};

>>>>>>> a955b0b (add cube)
export default App;
