export const uploadWorkforceData = async (fileData) => {
  const response = await fetch('http://localhost:4000/api/all/upload/', {
    method: 'POST',
    credentials: 'include',
    body: fileData
  });
  return response.json();
};
