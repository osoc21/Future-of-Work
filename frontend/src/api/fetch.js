/**
 * 
 * @returns csv data in JSON format
 */
export const fetchWorkforceData = async () => {
  const response = await fetch('http://localhost:4000/api/supply/calculate/', {
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
  const response = await fetch('http://localhost:4000/api/demand/parameters/', {
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
  const response = await fetch('http://localhost:4000/api/demand/calculate/', {
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
  const response = await fetch('http://localhost:4000/api/gap/calculate/', {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};
