import React, { useEffect, useRef } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

interface MagicCubeProps {
    magicCube: number[][][];
    algorithm: string;
}

function createNumberTexture(number: number): THREE.CanvasTexture {
    const size = 256;
    const canvas = document.createElement("canvas");
    canvas.width = size;
    canvas.height = size;
    const context = canvas.getContext("2d")!;
    context.fillStyle = "#FFFFFF";
    context.font = "bold 100px Arial";
    context.textAlign = "center";
    context.textBaseline = "middle";
    context.fillText(number.toString(), size / 2, size / 2);
    return new THREE.CanvasTexture(canvas);
}

const MagicCube: React.FC<MagicCubeProps> = ({ magicCube, algorithm }) => {
    const containerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        // Handle algorithm-specific logic
        console.log("Using algorithm:", algorithm);

        const w = 800;
        const h = 800;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(w, h);

        if (containerRef.current) {
            containerRef.current.appendChild(renderer.domElement);
        }

        const fov = 75;
        const aspect = w / h;
        const near = 0.1;
        const far = 100;
        const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
        camera.position.z = 10;

        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xdee2e6);

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.03;

        const cubeSize = 0.5;
        const spacing = 1;
        const parentCube = new THREE.Group();

        for (let x = 0; x < magicCube.length; x++) {
            for (let y = 0; y < magicCube[x].length; y++) {
                for (let z = 0; z < magicCube[x][y].length; z++) {
                    const number = magicCube[x][y][z];

                    const numberTexture = createNumberTexture(number);
                    const faceMaterials = Array(6).fill(new THREE.MeshBasicMaterial({ map: numberTexture }));

                    const smallCube = new THREE.Mesh(new THREE.BoxGeometry(cubeSize, cubeSize, cubeSize), faceMaterials);

                    smallCube.position.set(
                        (x - 2) * spacing,
                        (y - 2) * spacing,
                        (z - 2) * spacing
                    );

                    parentCube.add(smallCube);
                }
            }
        }

        scene.add(parentCube);

        const animate = () => {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        };
        animate();

        return () => {
            renderer.domElement.remove();
        };
    }, [magicCube, algorithm]);

    return <div ref={containerRef}></div>;
};

export default MagicCube;
