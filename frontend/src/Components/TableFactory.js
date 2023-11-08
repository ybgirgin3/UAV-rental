import React from 'react';
import './TableFactory.css';

const TableFactory = ({ data }) => {
  const columns = data.length > 0 ? Object.keys(data[0]) : [];

  return (
    <table>
      <thead>
        <tr>
          {columns.map((column, index) => (
            <th key={index}>{column}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((item, rowIndex) => (
          <tr key={rowIndex}>
            {columns.map((column, columnIndex) => (
              <td key={columnIndex}>{item[column]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TableFactory;
