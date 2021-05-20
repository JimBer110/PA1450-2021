var myChart = undefined;


fetch("http://" + window.location.hostname + ":8080/API/countries").then(response => {

  response.json().then(json => {

    const select = document.getElementById("countries");

    var countryList = json["countries"].slice();

    countryList.sort(function (a, b) {
      return a.toLowerCase().localeCompare(b.toLowerCase());
    });

    for (let i = 0; i < countryList.length; i++) {
      var opt = document.createElement('option');
      opt.value = countryList[i];
      opt.innerHTML = countryList[i];
      select.appendChild(opt);
    }

  });
});

var today = new Date();
var tmp = today.getFullYear();
if (today.getMonth()+1 < 10) {
  tmp += `-0${today.getMonth()+1}`;
} else {
  tmp += `-${today.getMonth()+1}`;
}
if (today.getDate() < 10) {
  tmp += `-0${today.getDate()}`;
} else {
  tmp += `-${today.getDate()}`;
}
today = tmp;

document.getElementById("updateForm").elements[1].value = "2020-01-21";
document.getElementById("updateForm").elements[2].value = today.toString();


fetch(`http://` + window.location.hostname + `:8080/API/confirmedCountryByDay/timespan/2020-01-21/${today}/NULL`)
.then(response => {

  response.json().then(json => {

    const labels = Object.keys(json["cases"]);

    var totalCases = [];
    for (var key in json["cases"]) {
      totalCases.push(json["cases"][key]);
    }

    var data = {
      labels: labels,
      datasets: [{
        label: 'Total Cases',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: totalCases
      }]
    };

    if ("vaccin" in json) {
      var totalVaccins = [];
      for (var key in json["vaccin"]) {
        totalVaccins.push(json["vaccin"][key]);
      }

      data["datasets"].push({
        label: 'Total Vaccinations',
        backgroundColor: 'rgb(30, 99, 132)',
        borderColor: 'rgb(30, 99, 132)',
        data: totalVaccins
      });
    }

    const config = {
      type: 'line',
      data,
      options: {}
    };

    myChart = new Chart(
      document.getElementById('totalCases'),
      config
    );
  });
});


function update() {

  const country = document.getElementById("updateForm").elements[0].value;
  const from = document.getElementById("updateForm").elements[1].value;
  const to = document.getElementById("updateForm").elements[2].value;

  fetch(`http://` + window.location.hostname + `:8080/API/confirmedCountryByDay/timespan/${from}/${to}/${country}`)
  .then(response => {

    response.json().then(json => {

      const labels = Object.keys(json["cases"]);

      var totalCases = []
      for (var key in json["cases"]) {
        totalCases.push(json["cases"][key])
      }

      var data = {
        labels: labels,
        datasets: [{
          label: 'Total Cases',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: totalCases,
        }]
      };

      if ("vaccin" in json) {
        var totalVaccins = [];
        for (var key in json["vaccin"]) {
          totalVaccins.push(json["vaccin"][key]);
        }

        data["datasets"].push({
          label: 'Total Vaccinations',
          backgroundColor: 'rgb(30, 99, 132)',
          borderColor: 'rgb(30, 99, 132)',
          data: totalVaccins
        });
      }

      const config = {
        type: 'line',
        data,
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      };

      myChart.destroy();

      myChart = new Chart(
        document.getElementById('totalCases'),
        config
      );
    });
  });
}
