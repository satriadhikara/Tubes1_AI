import React, { useEffect, useRef } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import { MagicCubeProps } from "../types";

function createNumberTexture(number: number): THREE.CanvasTexture {
  const size = 128; // Reduced from 256
  const canvas = document.createElement("canvas");
  canvas.width = size;
  canvas.height = size;
  const context = canvas.getContext("2d")!;
  context.fillStyle = "#FFFFFF";
  context.font = "bold 50px Arial"; // Reduced from 100px
  context.textAlign = "center";
  context.textBaseline = "middle";
  context.fillText(number.toString(), size / 2, size / 2);
  return new THREE.CanvasTexture(canvas);
}

const MagicCube: React.FC<MagicCubeProps> = ({ magic_cube }) => {
  const rendererRef = useRef<THREE.WebGLRenderer | null>(null);
  const sceneRef = useRef<THREE.Scene | null>(null);
  const cameraRef = useRef<THREE.PerspectiveCamera | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const controlsRef = useRef<OrbitControls | null>(null);
  const texturesRef = useRef<THREE.CanvasTexture[]>([]);

  const initialCameraPosition = new THREE.Vector3(0, 0, 3.5); // Reduced from 10

  useEffect(() => {
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xdee2e6);
    sceneRef.current = scene;

    const w = window.innerWidth / 3; // Reduced from /2
    const h = window.innerHeight / 2; // Reduced from 3/4
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(w, h);
    rendererRef.current = renderer;

    const camera = new THREE.PerspectiveCamera(75, w / h, 0.1, 1000);
    camera.position.copy(initialCameraPosition);
    cameraRef.current = camera;

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controlsRef.current = controls;

    if (containerRef.current) {
      containerRef.current.appendChild(renderer.domElement);
    }

    const cubeSize = 0.3; // Reduced from 0.5
    const spacing = 0.6; // Reduced from 1

    const parentCube = new THREE.Group();

    for (let x = 0; x < 5; x++) {
      for (let y = 0; y < 5; y++) {
        for (let z = 0; z < 5; z++) {
          const number = magic_cube[x][y][z];
          const texture = createNumberTexture(number);
          texturesRef.current.push(texture);

          const materials = Array(6).fill(
            new THREE.MeshBasicMaterial({ map: texture })
          );

          const smallCube = new THREE.Mesh(
            new THREE.BoxGeometry(cubeSize, cubeSize, cubeSize),
            materials
          );

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
      renderer.dispose();
      texturesRef.current.forEach((texture) => texture.dispose());
      scene.traverse((object) => {
        if (object instanceof THREE.Mesh) {
          object.geometry.dispose();
          if (Array.isArray(object.material)) {
            object.material.forEach((material) => material.dispose());
          } else {
            object.material.dispose();
          }
        }
      });
      if (containerRef.current && renderer.domElement) {
        containerRef.current.removeChild(renderer.domElement);
      }
    };
  }, [magic_cube]);

  const resetCamera = () => {
    if (cameraRef.current && controlsRef.current) {
      cameraRef.current.position.copy(initialCameraPosition);
      cameraRef.current.lookAt(0, 0, 0);
      controlsRef.current.reset();
    }
  };

  return (
    <div className="relative">
      <button
        onClick={resetCamera}
        className="absolute top-[35px] right-[15px] z-10 bg-black text-white px-3 py-1 rounded-lg hover:bg-gray-800 transition-colors text-sm"
      >
        Reset view
      </button>
      <div ref={containerRef} className="w-full h-full" />
    </div>
  );
};

export default MagicCube;
