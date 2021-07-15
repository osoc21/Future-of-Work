export const fetchWorkforceData = async () => {
  const response = await fetch('https://randomuser.me/api/?results=1', {
    method: 'GET'
  });
  return await response.json();
};
