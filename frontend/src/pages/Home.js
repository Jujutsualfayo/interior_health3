// src/pages/Home.js
import React from 'react';
import DrugList from '../components/DrugList.js';

const Home = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold text-center my-8">Welcome to the Interior Health App</h1>
      <DrugList />
    </div>
  );
};

export default Home;
