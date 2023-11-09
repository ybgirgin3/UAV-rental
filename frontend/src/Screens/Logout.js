import React from 'react';
import { Alert } from 'flowbite-react';

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
