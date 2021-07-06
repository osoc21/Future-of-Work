(() => {
  const API_URL = 'https://api.punkapi.com/v2/beers';
  const app = {
    init() {
      this.fetchData();
    },
    async fetchData() {
      const response = await fetch(API_URL);
      const data = await response.json();
      this.populateHTML(data);
    },
    populateHTML(data) {
      console.log(data)
    }
  };
  app.init();
})();