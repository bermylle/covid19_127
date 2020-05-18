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
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: [2478,5267,734,784,433]
        }
      ]
    },

};

var ctxa = document.getElementById("bar-graph-agegrp");
var chart = new Chart(ctxa, config);