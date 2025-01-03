import React, { useEffect, useState } from 'react';
import api from './services/api'; // Import the API service
import './styles/styles.css'; // Import custom styles

function App() {
  const [drugs, setDrugs] = useState([]);

  useEffect(() => {
    api.get('drugs/') // Replace 'drugs/'
      .then((response) => {
        console.log(response.data); // Log the data for testing
        setDrugs(response.data); // Save the data to state
      })
      .catch((error) => {
        console.error('Error fetching drugs:', error); // Log any errors
      });
  }, []);

  return (
    <div>
      <h1>Interior Health App</h1>
      <h2>Available Drugs</h2>
      {drugs.length > 0 ? (
        <ul>
          {drugs.map((drug) => (
            <li key={drug.id}>
              <span>{drug.name}</span>
              <span>${drug.price}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p>No drugs available at the moment.</p>
      )}
    </div>
  );
}

export default App;
