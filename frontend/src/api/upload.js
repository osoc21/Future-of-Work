export const uploadWorkforceData = async (fileData) => {
  const response = await fetch('http://localhost:4000/api/supply/upload/', {
    method: 'POST',
    credentials: 'include',
    body: fileData
  });
  return await response.json();
};
