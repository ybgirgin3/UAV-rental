import React from 'react';
import { Alert } from 'flowbite-react';

/**
 * Logout Component
 * Logs the user out and displays a confirmation message.
 *
 * @returns {JSX.Element} The Logout component.
 */

export default function Logout() {
  localStorage.removeItem('access_token');
  return (
    <div>
      <Alert color="failure">
        <span className="font-medium">Info alert!</span>
        You logged out
      </Alert>
    </div>
  );
}
