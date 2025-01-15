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
    <div className="p-4">
      <h1 className="text-xl font-semibold mb-4">List of Drugs</h1>
      <ul>
        {drugs.map((drug) => (
          <li key={drug.id} className="border-b py-2">
            <p>{drug.name}</p>
            <p>{drug.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DrugList;
