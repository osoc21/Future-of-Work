export const fetchWorkforceData = async () => {
  const response = await fetch('http://localhost:4000/api/supply/calculate/', {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

export const fetchDemandParameters = async () => {
  const response = await fetch('http://localhost:4000/api/demand/parameters/', {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};

export const fetchDemandData = async () => {
  const response = await fetch('http://localhost:4000/api/demand/calculate/', {
    method: 'GET',
    credentials: 'include'
  });
  return response.json();
};
