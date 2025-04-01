function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      const response = {
        firstName: 'Guillaume',
        lastName: 'Salva',
      };

      resolve(response);
    });
  }

  export default getResponseFromAPI;
