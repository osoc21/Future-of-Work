export const uploadWorkforceData = async (fileData) => {
  const response = await fetch('http://localhost:4000/API/upload/', {
    method: 'POST',
    mode: 'no-cors',
    // credentials: 'same-origin',
    body: fileData
  });
  return response.json();
};
