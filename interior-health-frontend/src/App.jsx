import React from 'react';
import './styles/styles.css'; // Import custom styles
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Add Router for routing
import DrugsList from './pages/DrugsList'; // Import DrugsList

function App() {
  return (
    <Router>
      <div className="container">
        <h1>Interior Health App</h1>
        <h2>Available Drugs</h2>
        <Routes>
          <Route path="/" element={<DrugsList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
