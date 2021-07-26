export const postParameterData = async (id, year, value) => {
  const response = await fetch(`http://localhost:4000/${year}/${id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      parameter: value
    })
  });
  return response.json();
};
