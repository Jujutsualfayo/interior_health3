import React from 'react';
import { Link } from 'react-router-dom';  // Importing Link from react-router-dom to navigate between pages

const Navbar = () => {
  return (
    <nav className="bg-blue-500 p-4">
      <ul className="flex justify-around text-white">
        <li>
          <Link to="/" className="hover:text-gray-300">Home</Link>
        </li>
        <li>
          <Link to="/login" className="hover:text-gray-300">Login</Link>
        </li>
        <li>
          <Link to="/drugs" className="hover:text-gray-300">Drugs</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
