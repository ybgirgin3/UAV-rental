import React from 'react';
import { NavLink } from 'react-router-dom';

/**
 * Header Component
 * Renders a navigation bar with links to different pages.
 *
 * @returns {JSX.Element} The Header component.
 */

export default function Header() {
  const styles = {
    navStyle: {
      display: 'flex',
      flexDirection: 'row',
      justifyContent: 'center',
      fontSize: '20px',
      background: '#6666',
      color: '#000',
    },
    navLinkStyle: {
      margin: '10px',
    },
  };
  return (
    <nav style={styles.navStyle}>
      <NavLink style={styles.navLinkStyle} to="/">
        UAV
      </NavLink>
      <NavLink style={styles.navLinkStyle} to="/create">
        Create Reservation
      </NavLink>
      <NavLink style={styles.navLinkStyle} to="/register">
        Register
      </NavLink>
      <NavLink style={styles.navLinkStyle} to="/login">
        Login
      </NavLink>
      <NavLink style={styles.navLinkStyle} to="/logout">
        Logout
      </NavLink>
    </nav>
  );
}
