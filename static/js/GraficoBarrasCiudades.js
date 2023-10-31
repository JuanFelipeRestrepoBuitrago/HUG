am5.ready(function() {
  // Crear el elemento raíz
  var root = am5.Root.new("chartdiv");

  // Establecer temas
  root.setThemes([
    am5themes_Animated.new(root)
  ]);

  // Crear el gráfico de pastel
  var chart = root.container.children.push(am5percent.PieChart.new(root, {
    layout: root.verticalLayout
  }));


  // Crear la serie de pastel
  var series = chart.series.push(am5percent.PieSeries.new(root, {
    valueField: "total_egresados",
    categoryField: "ciudad",
    alignLabels: false
  }));


  // Obtener los datos y establecerlos en la serie
series.data.setAll([{
  category: "Lithuania",
  value: 501.9
}, {
  category: "Czechia",
  value: 301.9
}, {
  category: "Ireland",
  value: 201.1
}, {
  category: "Germany",
  value: 165.8
}, {
  category: "Australia",
  value: 139.9
}, {
  category: "Austria",
  value: 128.3
}, {
  category: "UK",
  value: 99
}]);

  series.labels.template.setAll({
    visible: false
  });
});
