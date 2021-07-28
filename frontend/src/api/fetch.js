import { API_URL } from '../constants';

export const fetchWorkforceData = async () => {
  const response = await fetch(`${API_URL}/supply/calculate/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

export const fetchDemandParameters = async () => {
  const response = await fetch(`${API_URL}/demand/parameters/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

export const fetchDemandData = async () => {
  const response = await fetch(`${API_URL}/demand/calculate/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

export const fetchGapData = async () => {
  const response = await fetch(`${API_URL}/gap/calculate/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};
