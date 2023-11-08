import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import './App.css';
import HomeScreen from './Screens/HomeScreen';
import Login from './Screens/Login';
import Header from './Components/Header';
import Register from './Screens/Register';
import Logout from './Screens/Logout';
import CreateScreen from './Screens/CreateScreen';

function App() {
  return (
    <React.StrictMode>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" Component={HomeScreen} />
          <Route path="/create" Component={CreateScreen} />
          <Route path="/login" Component={Login} />
          <Route path="/register" Component={Register} />
          <Route path="/logout" Component={Logout} />
        </Routes>
      </BrowserRouter>
    </React.StrictMode>
  );
}

export default App;
