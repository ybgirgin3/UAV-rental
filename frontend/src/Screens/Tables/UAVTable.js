import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TableFactory from '../../Components/TableFactory';

function UAVTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/uav/')
      .then((response) => {
        setData(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error('Veri alınamadı: ', error);
      });
  }, []);
  return (
    <div>
      <h1>UAVs</h1>
      <TableFactory data={data} />
    </div>
  );
}

export default UAVTable;
