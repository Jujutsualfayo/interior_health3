import React, { useEffect, useState } from 'react';
import api from '../services/api'; // Import the API service
import "../styles/styles.css"; // One level up to src


const DrugsList = () => {
  const [drugs, setDrugs] = useState([]);
  const [loading, setLoading] = useState(true); // Loading state to show a loader
  const [error, setError] = useState(null); // Error state to show error message

  useEffect(() => {
    api.get('drugs/') // Replace 'drugs/' with the correct endpoint if needed
      .then((response) => {
        console.log(response.data); // Log the data for testing
        setDrugs(response.data); // Save the data to state
        setLoading(false); // Data is loaded, hide loader
      })
      .catch((error) => {
        console.error('Error fetching drugs:', error); // Log any errors
        setError('Failed to fetch data. Please try again later.'); // Set error message
        setLoading(false); // Hide loader
      });
  }, []);

  return (
    <div>
      {/* Show loading spinner while data is being fetched */}
      {loading && <div className="loading">Loading...</div>}

      {/* Display error message if data fetching fails */}
      {error && <div className="error">{error}</div>}

      {/* Display list of drugs */}
      {drugs.length > 0 ? (
        <ul className="drug-list">
          {drugs.map((drug) => (
            <li key={drug.id} className="drug-item">
              <div className="drug-name">{drug.name}</div>
              <div className="drug-price">${drug.price}</div>
            </li>
          ))}
        </ul>
      ) : (
        <p>No drugs available at the moment.</p>
      )}
    </div>
  );
};

export default DrugsList;
