import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

/**
 * Login Component
 * Allows users to log in with a username and password.
 *
 * @returns {JSX.Element} The Login component.
 */

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const handleLogin = () => {
    localStorage.setItem('username', username);
    axios
      .post('http://localhost:8000/auth/token/', { username, password })
      .then((response) => {
        console.log('login successfull', response.data);
        const token = response.data.access;
        localStorage.setItem('access_token', token);
        navigate('/');
      })
      .catch((error) => {
        console.log('unable to login');
      });
  };

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        display: 'flex',
        justifyContent: 'center',
      }}>
      <div class="w-full max-w-xs">
        <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div class="mb-4">
            <label
              class="block text-gray-700 text-sm font-bold mb-2"
              for="username">
              Username
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="email"
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div class="mb-6">
            <label
              class="block text-gray-700 text-sm font-bold mb-2"
              for="password">
              Password
            </label>
            <input
              class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              id="password"
              type="password"
              placeholder="******************"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div class="flex items-center justify-between">
            <button
              onClick={handleLogin}
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button">
              Sign In
            </button>
          </div>
        </form>
      </div>
    </div>
    // <div>
    //   <h2>Kullanıcı Kaydı</h2>
    //   <input
    //     type="text"
    //     placeholder="Kullanıcı Adı"
    //     value={username}
    //     onChange={(e) => setUsername(e.target.value)}
    //   />
    //   <input
    //     type="password"
    //     placeholder="Şifre"
    //     value={password}
    //     onChange={(e) => setPassword(e.target.value)}
    //   />

    //   <h2>Kullanıcı Girişi</h2>
    //   <button onClick={handleLogin}>Giriş Yap</button>
    // </div>
  );
}
