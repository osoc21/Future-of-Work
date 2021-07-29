import { API_URL } from '../constants';

export const uploadWorkforceData = async (fileData) => {
  const response = await fetch(`${API_URL}/all/upload/`, {
    method: 'POST',
    credentials: 'include',
    body: fileData
  });
  return response.json();
};
