// [Data Set A]
// Line graph 
var config = {
   options: {
    title: {
      display: true,
      text: 'COVID19 Cases in the Philippines'
    },
    scales: {
        yAxes: [{
            display: true,
            ticks: {
            }
        }]
    }
  },
   type: 'line',
  data: {
    labels: ph_dates,
    datasets: [{ 
        data: ph_confirmed,
        label: 'Confirmed Cases',
        borderColor: "#c45850",
        fill: false
      }, { 
        data: ph_recoveries,
        label: 'Recoveries',
        borderColor: "#3cba9f",
        fill: false
      }, { 
        data: ph_deaths,
        label: 'Deaths',
        borderColor: "#e8c3b9",
        fill: false
      }
    ]
  }
};
var ctx = document.getElementById("line-chart-ph");
var chart = new Chart(ctx, config);

// [Data Set A] 
// Bar graph [Confirmed Cases] 
var config = {
   options: {
      title: {
        display: true,
        text: 'Confirmed Cases in PH,CHN,SGP,MYS,PRK'
      },
      scales: {
          xAxes: [{
              
          }],
          yAxes: [{
              
          }]
      }
    },
   type: 'bar',
      data: {
      labels: ["Total Confirmed Cases"],
      datasets: [
        {
          label: "Philippines",
          backgroundColor: "#eb6383",
          data: [ph_confirmed_total]
        }, {
          label: "Indonesia",
          backgroundColor: "#fa9191",
          data: [ind_confirmed_total]
        }, {
          label: "Singapore",
          backgroundColor: "#ffe9c5",
          data: [sgp_confirmed_total]
        }, {
          label: "Malaysia",
          backgroundColor: "#b4f2e1",
          data: [mys_confirmed_total]
        }, {
          label: "Korea",
          backgroundColor: "#58b4ae",
          data: [prk_confirmed_total]
        },
      ]
    },

};

var ctx = document.getElementById("bar-chart-confirmed-cases");
var chart = new Chart(ctx, config);

// Bar graph [Recovered Cases] 
var config = {
   options: {
      title: {
        display: true,
        text: 'Total Recoveries in PH,CHN,SGP,MYS,PRK'
      },
      scales: {
          xAxes: [{
              
          }],
          yAxes: [{
              
          }]
      }
    },
   type: 'bar',
      data: {
      labels: ["Total Recoveries"],
      datasets: [
        {
          label: "Philippines",
          backgroundColor: "#eb6383",
          data: [ph_recoveries_total]
        }, {
          label: "Indonesia",
          backgroundColor: "#fa9191",
          data: [ind_recoveries_total]
        }, {
          label: "Singapore",
          backgroundColor: "#ffe9c5",
          data: [sgp_recoveries_total]
        }, {
          label: "Malaysia",
          backgroundColor: "#b4f2e1",
          data: [mys_recoveries_total]
        }, {
          label: "Korea",
          backgroundColor: "#58b4ae",
          data: [prk_recoveries_total]
        },
      ]
    },

};

var ctx = document.getElementById("bar-chart-recovery-cases");
var chart = new Chart(ctx, config);

// Bar graph [Total Death Cases] 
var config = {
   options: {
      title: {
        display: true,
        text: 'Total Deaths in PH,CHN,SGP,MYS,PRK'
      },
      scales: {
          xAxes: [{
              
          }],
          yAxes: [{
              
          }]
      }
    },
   type: 'bar',
      data: {
      labels: ["Total Deaths"],
      datasets: [
        {
          label: "Philippines",
          backgroundColor: "#eb6383",
          data: [ph_deaths_total]
        }, {
          label: "Indonesia",
          backgroundColor: "#fa9191",
          data: [ind_deaths_total]
        }, {
          label: "Singapore",
          backgroundColor: "#ffe9c5",
          data: [sgp_deaths_total]
        }, {
          label: "Malaysia",
          backgroundColor: "#b4f2e1",
          data: [mys_deaths_total]
        }, {
          label: "Korea",
          backgroundColor: "#58b4ae",
          data: [prk_deaths_total]
        },
      ]
    },

};

var ctx = document.getElementById("bar-chart-death-cases");
var chart = new Chart(ctx, config);
//document.getElementById("demo").innerHTML = ph_confirmed;

