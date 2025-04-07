
import axios from 'axios';

const API_URL = 'http://localhost:5000/api/';

// Login function to get JWT token
export const login = async (email, role) => {
    const response = await axios.post(`${API_URL}login`, { email, role });
    if (response.data.access_token) {
        localStorage.setItem('access_token', response.data.access_token);
    }
    return response;
};

// Add Item function
export const addItem = async (itemData) => {
    const token = localStorage.getItem('access_token');
    const response = await axios.post(`${API_URL}add_item`, itemData, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });
    return response;
};

// View Items function
export const viewItems = async () => {
    const token = localStorage.getItem('access_token');
    const response = await axios.get(`${API_URL}view_items`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });
    return response.data;
};
