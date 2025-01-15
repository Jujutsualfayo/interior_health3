// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Replace with your backend API base URL
});

// DRUGS API
export const getDrugs = () => {
  return api.get('drugs/');  // Get list of all drugs
};

export const createDrug = (drugData) => {
  return api.post('drugs/', drugData);  // Create a new drug
};

export const getDrugById = (id) => {
  return api.get(`drugs/${id}/`);  // Get details of a specific drug
};

// USERS API
export const getUserProfile = (userId) => {
  return api.get(`users/${userId}/profile/`);  // Get a user's profile details
};

export const login = (credentials) => {
  return api.post('users/login/', credentials);  // User login
};

export const registerUser = (userData) => {
  return api.post('users/register/', userData);  // Register a new user
};

export const updateUserProfile = (userId, profileData) => {
  return api.put(`users/${userId}/profile/`, profileData);  // Update user's profile
};

// ORDERS API
export const getOrders = () => {
  return api.get('orders/');  // Get all orders
};

export const createOrder = (orderData) => {
  return api.post('orders/', orderData);  // Create a new order
};

export const getOrderById = (id) => {
  return api.get(`orders/${id}/`);  // Get a specific order by ID
};

export const updateOrder = (id, orderData) => {
  return api.put(`orders/${id}/`, orderData);  // Update an existing order
};

export const deleteOrder = (id) => {
  return api.delete(`orders/${id}/`);  // Delete an order by ID
};

// Default export
export default api;
