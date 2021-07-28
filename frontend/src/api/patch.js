import { API_URL } from '../constants';

export const postParameterData = async (id, year, value) => {
  const response = await fetch(`${API_URL}/demand/parameter/${year}/${id}`, {
    method: 'PATCH',
    credentials: 'include',
    body: JSON.stringify({
      parameter: value
    })
  });
  return response.json();
};
