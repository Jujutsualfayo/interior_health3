import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DrugList = () => {
  const [drugs, setDrugs] = useState([]);

  useEffect(() => {
    // Fetch drugs from the API
    axios.get('http://localhost:8000/api/drugs/')
      .then(response => {
        setDrugs(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the drugs!", error);
      });
  }, []);

  return (
    <div className="p-6 bg-white shadow-lg rounded-lg">
      <h1 className="text-3xl font-semibold text-gray-800 mb-6">List of Drugs</h1>
      <ul>
        {drugs.length > 0 ? (
          drugs.map((drug) => (
            <li key={drug.id} className="border-b py-4 mb-4 last:border-b-0">
              <h2 className="text-xl font-medium text-gray-900">{drug.name}</h2>
              <p className="text-gray-600 mt-1">{drug.description}</p>
            </li>
          ))
        ) : (
          <p className="text-center text-gray-500">No drugs available.</p>
        )}
      </ul>
    </div>
  );
};

export default DrugList;
