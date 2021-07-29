/**
 * 
 * @returns csv data in JSON format
 */

import { API_URL } from '../constants';

export const fetchWorkforceData = async () => {
  const response = await fetch(`${API_URL}/supply/calculate/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

/**
 * 
 * @returns demand parameters from demand.csv file
 */
export const fetchDemandParameters = async () => {
  const response = await fetch(`${API_URL}/demand/parameters/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

/**
 * 
 * @returns calculated FTEs per Job title in JSON  format
 */
export const fetchDemandData = async () => {
  const response = await fetch(`${API_URL}/demand/calculate/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};
 /**
  * 
  * @returns difference between Supply and Demand FTEs amounts per Job title in JSON format
  */
export const fetchGapData = async () => {
  const response = await fetch(`${API_URL}/gap/calculate/`, {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};
