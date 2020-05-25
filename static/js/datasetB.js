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
          label: "Number of Patients",
          backgroundColor: '#3e95cd',
          data: data
        }
      ]
    },

};

var ctxa = document.getElementById("bar-graph-agegrp");
var chart = new Chart(ctxa, config);

// doughnut chart [Total # per Sex] 
var config = {
   options: {
      title: {
        display: true,
        text: 'Number of patients per Sex'
      }
    },
   type: 'doughnut',
    data: {
      labels: labels_sex,
      datasets: [
        {
          label: "Number of Patients",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: data_sex
        }
      ]
    },

};

var ctxa = document.getElementById("doughnut-chart-sex");
var chart = new Chart(ctxa, config);

// bar chart [Total # per rpr] 
var config = {
   options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Number of patients per Region/Province'
      }
    },
    type: 'horizontalBar',
   data: {
      labels: labels_rpr,
      datasets: [
        {
          label: "Number of Patients",
          backgroundColor: "#3e95cd",
          data: data_rpr
        }
      ]
    },

};

var ctxa = document.getElementById("bar-chart-grouped-location-rpr");
var chart = new Chart(ctxa, config);

// bar chart [Total # per mcr] 
var config = {
   options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Number of patients per Municipality/City/Residence'
      }
    },
    type: 'horizontalBar',
   data: {
      labels: labels_mcr,
      datasets: [
        {
          label: "Population (millions)",
          backgroundColor: "#3e95cd",
          data: data_mcr
        }
      ]
    },

};

var ctxa = document.getElementById("bar-chart-grouped-location-mcr");
var chart = new Chart(ctxa, config);

$(document).ready( function () {
    $('#table_data').DataTable();
} );
