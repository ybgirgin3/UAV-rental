import React, { useState, useEffect } from 'react';
import {
  Button,
  Form,
  Input,
  Radio,
  DatePicker,
  InputNumber,
  Select,
} from 'antd';
import axios from 'axios';

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
    values['issue_date'] = values['issue_date_datetime'].toLocalDateString;
    values['return_date'] = values['return_date_datetime'].toLocalDateString;
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
            <Select.Option value={item.name}>{item.name}</Select.Option>
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
        <DatePicker />
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
        <DatePicker />
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
}
