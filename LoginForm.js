
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { login } from '../api';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [role, setRole] = useState('lister');
  const history = useHistory();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await login(email, role);
      if (response.data.access_token) {
        history.push('/lister-dashboard');  // Redirect to lister dashboard after successful login
      }
    } catch (err) {
      alert('Login failed! Please check your credentials and try again.');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      <select value={role} onChange={(e) => setRole(e.target.value)}>
        <option value="lister">Lister</option>
        <option value="collector">Collector</option>
      </select>
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;
