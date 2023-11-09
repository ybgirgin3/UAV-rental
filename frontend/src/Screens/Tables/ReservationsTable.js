import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TableFactory from '../../Components/TableFactory';

/**
 * ReservationsTable Component
 * Fetches and displays a table of reservations data from the API.
 *
 * @returns {JSX.Element} The ReservationsTable component.
 */

function ReservationsTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/reservation/')
      .then((response) => {
        setData(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error('Unable to Fetch Data: ', error);
      });
  }, []);
  return (
    <div>
      <h1>Reservations</h1>
      <TableFactory data={data} />
    </div>
  );
}

export default ReservationsTable;
