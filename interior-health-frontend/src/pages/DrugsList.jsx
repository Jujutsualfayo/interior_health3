import React, { useEffect, useState } from 'react';
import api from '../services/api';

const DrugsList = () => {
    const [drugs, setDrugs] = useState([]);

    useEffect(() => {
        api.get('drugs/')
            .then((response) => setDrugs(response.data))
            .catch((error) => console.error(error));
    }, []);

    return (
        <div>
            <h1>Available Drugs</h1>
            <ul>
                {drugs.map((drug) => (
                    <li key={drug.id}>
                        {drug.name} - ${drug.price}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DrugsList;
