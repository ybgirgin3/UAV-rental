import React from 'react';
import './TableFactory.css';

const TableFactory = ({ data }) => {
  const columns = data.length > 0 ? Object.keys(data[0]) : [];
  console.log('data in tablefactory', data);
  console.log('column in tablefactory', columns);

  if (data.length > 0) {
    return (
      <div>
        <table class="table-auto">
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
      </div>
    );
  } else {
    return <div>No Data Found</div>;
  }
};

export default TableFactory;
