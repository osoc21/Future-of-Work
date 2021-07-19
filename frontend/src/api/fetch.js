export const fetchWorkforceData = async () => {
  const response = await fetch('http://localhost:4000/API/load/', {
    method: 'GET',
    credentials: "include"
  });
  return await response.json();

  
};
