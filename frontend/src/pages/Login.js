// src/pages/Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const credentials = { email, password };

    axios.post('http://localhost:8000/users/login/', credentials)
      .then(response => {
        // Assuming a token is returned upon successful login
        localStorage.setItem('token', response.data.token);
        navigate('/');  // Redirect to home after successful login
      })
      .catch(error => {
        console.error("There was an error logging in!", error);
      });
  };

  return (
    <div className="max-w-md mx-auto mt-8 p-4 border rounded shadow">
      <h2 className="text-2xl mb-4">Login</h2>
      <form onSubmit={handleSubmit}>
        <input 
          type="email" 
          className="w-full p-2 mb-4 border rounded" 
          placeholder="Email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <input 
          type="password" 
          className="w-full p-2 mb-4 border rounded" 
          placeholder="Password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        />
        <button 
          type="submit" 
          className="w-full bg-blue-500 text-white p-2 rounded"
        >
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
