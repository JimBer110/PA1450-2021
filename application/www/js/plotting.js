fetch("http://localhost:8080/API/confirmedCountryByDay/timespan/2020-02-03/2021-05-02/NULL")
  .then(response => {

    response.json().then(json => {

      const labels = Object.keys(json);

      var totalCases = []
      for (var key in json) {
        totalCases.push(json[key])
      }

      const data = {
        labels: labels,
        datasets: [{
          label: 'Total Cases',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: totalCases,
        }]
      };

      const config = {
        type: 'line',
        data,
        options: {}
      };

      var myChart = new Chart(
        document.getElementById('totalCases'),
        config
      );
    });
  });
