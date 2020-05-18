// Bar graph [Total # per Age group] 
var config = {
   options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Number of patients per Age Group'
      }
    },
   type: 'horizontalBar',
    data: {
      labels: labels,
      datasets: [
        {
          label: "Population (millions)",
          backgroundColor: '#3e95cd',
          data: data
        }
      ]
    },

};

var ctxa = document.getElementById("bar-graph-agegrp");
var chart = new Chart(ctxa, config);