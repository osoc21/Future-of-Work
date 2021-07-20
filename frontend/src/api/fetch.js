export const fetchWorkforceData = async () => {
  const response = await fetch('http://localhost:4000/api/supply/', {
    method: 'GET',
    credentials: "include"
  });
  return await response.json();

  
};
