// src/__tests__/Login.test.js
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Login from '../components/Login';

test('renders Login form and submits the correct data', () => {
  const mockSubmit = jest.fn();
  render(<Login onSubmit={mockSubmit} />);

  // Find elements
  const usernameInput = screen.getByPlaceholderText(/username/i);
  const passwordInput = screen.getByPlaceholderText(/password/i);
  const submitButton = screen.getByRole('button', { name: /login/i });

  // Simulate user input
  fireEvent.change(usernameInput, { target: { value: 'testUser' } });
  fireEvent.change(passwordInput, { target: { value: 'testPassword' } });

  // Submit form
  fireEvent.click(submitButton);

  // Check if the mock function is called with the correct values
  expect(mockSubmit).toHaveBeenCalledWith('testUser', 'testPassword');
});

