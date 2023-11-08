import React, { useEffect, useState } from 'react';

import { Tabs } from 'antd';
import TabPane from 'antd/es/tabs/TabPane';
import UAVTable from './Tables/UAVTable';
import ReservationsTable from './Tables/ReservationsTable';

function HomeScreen() {
  if (localStorage.getItem('access_token') !== null) {
    return (
      <div>
        <Tabs centered defaultActiveKey="1" type="card" size="large">
          <TabPane key={1} tab={'UAV'}>
            <UAVTable />
          </TabPane>
          <TabPane key={2} tab={'Reservation'}>
            <ReservationsTable />
          </TabPane>
        </Tabs>
      </div>
    );
  } else {
    return <div>You need to login to see UAV table</div>;
  }
}

export default HomeScreen;
