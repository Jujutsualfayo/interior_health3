import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom'; // Import Router for routing functionality
import App from './App';

test('renders login link', () => {
  render(
    <Router>  {/* Wrap the App component in a Router to simulate routing */}
      <App />
    </Router>
  );
  const loginLink = screen.getByText(/login/i);  // Check for the "login" link text
  expect(loginLink).toBeInTheDocument();  // Verify that the "login" link is in the document
});
