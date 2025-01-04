import React, { useEffect, useState } from 'react';
import api from './services/api';
import '../styles/styles.css'; // Import custom styles

const DrugsList = () => {
  const [drugs, setDrugs] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.get('drugs/')
      .then((response) => {
        console.log('API Response:', response.data); // Log API data
        setDrugs(response.data);
      })
      .catch((err) => {
        console.error('Error fetching drugs:', err);
        setError('Failed to load drugs');
      });
  }, []);

  return (
    <div>
      <h3>Drugs List Page</h3> {/* Debug message */}
      {error && <p className="error-message">{error}</p>}
      {drugs.length > 0 ? (
        <ul>
          {drugs.map((drug) => (
            <li key={drug.id}>
              <strong>{drug.name}</strong> - ${drug.price}
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
