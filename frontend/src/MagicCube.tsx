import React, { useEffect } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

const magic_cube = [
    [
        [25, 16, 80, 104, 90],
        [115, 98, 4, 1, 97],
        [42, 111, 85, 2, 75],
        [66, 72, 27, 102, 48],
        [67, 18, 119, 106, 5],
    ],
    [
        [91, 77, 71, 6, 70],
        [52, 64, 117, 69, 13],
        [30, 118, 21, 123, 23],
        [26, 39, 92, 44, 114],
        [116, 17, 14, 73, 95],
    ],
    [
        [47, 61, 45, 76, 86],
        [107, 43, 38, 33, 94],
        [89, 68, 63, 58, 37],
        [32, 93, 88, 83, 19],
        [40, 50, 81, 65, 79],
    ],
    [
        [31, 53, 112, 109, 10],
        [12, 82, 34, 87, 100],
        [103, 3, 105, 8, 96],
        [113, 57, 9, 62, 74],
        [56, 120, 55, 49, 35],
    ],
    [
        [121, 108, 7, 20, 59],
        [29, 28, 122, 125, 11],
        [51, 15, 41, 124, 84],
        [78, 54, 99, 24, 60],
        [36, 110, 46, 22, 101],
    ],
];

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

const MagicCube: React.FC = () => {
    useEffect(() => {
        const w = window.innerWidth;
        const h = window.innerHeight;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(w, h);
        document.body.appendChild(renderer.domElement);

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

        for (let x = 0; x < 5; x++) {
            for (let y = 0; y < 5; y++) {
                for (let z = 0; z < 5; z++) {
                    const number = magic_cube[x][y][z];

                    // Create a texture for each face
                    const numberTexture = createNumberTexture(number);
                    const faceMaterials = Array(6).fill(new THREE.MeshBasicMaterial({ map: numberTexture }));

                    // Create the cube with each face showing the number
                    const smallCube = new THREE.Mesh(new THREE.BoxGeometry(cubeSize, cubeSize, cubeSize), faceMaterials);

                    // Position the cube in 3D space
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
    }, []);

    return null;
};

export default MagicCube;
