import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';  
import Login from './pages/Login';  
import Home from './pages/Home';  

test('renders login link', () => {
  render(
    <Router>
      <App />
    </Router>
  );
  const loginLink = screen.getByText(/login/i);  // Assuming there's a "Login" link
  expect(loginLink).toBeInTheDocument();
});

test('login form submits correctly', async () => {
  render(
    <Router>
      <Login />
    </Router>
  );

  const usernameInput = screen.getByLabelText(/username/i);
  const passwordInput = screen.getByLabelText(/password/i);
  const submitButton = screen.getByRole('button', { name: /login/i });

  fireEvent.change(usernameInput, { target: { value: 'testuser' } });
  fireEvent.change(passwordInput, { target: { value: 'password123' } });
  fireEvent.click(submitButton);

  // Wait for the next page to be rendered (e.g., after login)
  await waitFor(() => screen.getByText(/welcome/i));
  expect(screen.getByText(/welcome/i)).toBeInTheDocument();
});

test('renders home page correctly after login', async () => {
  render(
    <Router>
      <App />
    </Router>
  );

  // Simulate navigating to the home page (e.g., after login)
  const loginLink = screen.getByText(/login/i);
  fireEvent.click(loginLink);

  // Fill out login form and submit
  fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'testuser' } });
  fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  // After login, check if home page elements are rendered
  await waitFor(() => screen.getByText(/home/i));  // Adjust based on the content of the home page
  expect(screen.getByText(/home/i)).toBeInTheDocument();
});
