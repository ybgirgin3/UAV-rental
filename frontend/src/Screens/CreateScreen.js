import React, { useState, useEffect } from 'react';
import { Button, Form, Input, DatePicker, Select } from 'antd';
import axios from 'axios';
import moment from 'moment';

/**
 * CreateScreen Component
 * Allows users to create reservations.
 *
 * @returns {JSX.Element} The CreateScreen component.
 */

export default function CreateScreen() {
  const [uav, setUav] = useState([]);
  const [data, setData] = useState([]);

  // get uav list
  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/uav/')
      .then((response) => {
        setUav(response.data);
        console.log('uav data', response.data);
      })
      .catch((error) => {
        console.error('Unable to Fetch UAV Data: ', error);
      });
  }, []);

  const handleSubmission = (values) => {
    values['is_deleted'] = false;
    values['issue_date'] = moment(values['issue_date_datetime']).format(
      'YYYY-MM-DD',
    );
    values['return_date'] = moment(values['return_date_datetime']).format(
      'YYYY-MM-DD',
    );
    values['customer'] = 1;
    console.log('values', values);

    axios
      .post('http://127.0.0.1:8000/api/reservation/', values)
      .then((res) => {
        console.log(res.data);
        setData(res.data);
      })
      .catch((e) => console.warn(e));

    return data;
  };

  if (localStorage.getItem('access_token') !== null) {
    // if access token is in localstore (that means user not logged out)
    return (
      <Form
        name="basic"
        labelCol={{
          span: 8,
        }}
        wrapperCol={{
          span: 16,
        }}
        style={{
          maxWidth: 600,
        }}
        initialValues={{
          remember: true,
        }}
        onFinish={handleSubmission}
        autoComplete="on">
        <Form.Item
          label="UAV"
          name="uav"
          rules={[{ required: true, message: 'Please select a uav' }]}>
          <Select>
            {uav.map((item) => (
              <Select.Option value={item.id}>{item.name}</Select.Option>
            ))}
          </Select>
        </Form.Item>
        <Form.Item
          label="Customer Name"
          name="customer"
          rules={[
            {
              required: true,
              message: 'Please insert a valid name!',
            },
          ]}>
          <Input placeholder={localStorage.getItem('username')} />
        </Form.Item>

        <Form.Item
          label="IssueDate"
          name="issue_date_datetime"
          rules={[
            {
              required: true,
              message: 'Please select a date!',
            },
          ]}>
          <DatePicker format="YYYY-MM-DD" />
        </Form.Item>

        <Form.Item
          label="Return Date"
          name="return_date_datetime"
          rules={[
            {
              required: true,
              message: 'Please select a date!',
            },
          ]}>
          <DatePicker format="YYYY-MM-DD" />
        </Form.Item>

        <Form.Item
          wrapperCol={{
            offset: 8,
            span: 16,
          }}>
          <Button type="secondary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    );
  } else {
    return <div>You need to login to book a reservation</div>;
  }
}
