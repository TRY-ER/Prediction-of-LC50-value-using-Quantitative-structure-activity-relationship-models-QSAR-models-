import './style.css';
import React, { Suspense } from "react";
import { Routes, Route, Link } from 'react-router-dom';
import { Predictor } from "./Predictor";


function App() {
  return(
    <div>
    <Routes >
      <Route exact path="/" element={<Predictor />} />
    </Routes>
    </div>
  );
}

export default App;

