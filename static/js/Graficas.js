
/**}
 * Documentación para el script de generado de graficas
 * @param {string} nombre
 * @param {HTMLElement} root
 * @param {string} valueField
 * @param {string} categoryField
 */
const fetchAndSetGrafica = (nombre, root, valueField, categoryField) => {
  if(root.firstChild) root.removeChild(root.firstChild);

  // Create chart
  // https://www.amcharts.com/docs/v5/charts/percent-charts/pie-chart/
  const chart = root.container.children.push(am5percent.PieChart.new(root, {
    layout: root.verticalLayout
  }));

  // Create series
  // https://www.amcharts.com/docs/v5/charts/percent-charts/pie-chart/#Series
  const series = chart.series.push(
    am5percent.PieSeries.new(root, {
      valueField,
      categoryField,
      alignLabels: false
    })
  );

  // Disable labels
  // https://www.amcharts.com/docs/v5/charts/percent-charts/pie-chart/#Disabling_labels
  series.labels.template.setAll({
    visible: false,
  });


  fetch(nombre)
    .then(response => response.json())
    .then(data => {
      series.data.setAll(data);
    })
    .catch(error => console.error("Error al obtener los datos:", error));
}

am5.ready(function () {

  // Create root element
  // https://www.amcharts.com/docs/v5/getting-started/#Root_element
  var root = am5.Root.new("chartdiv1");

  // Set themes
  // https://www.amcharts.com/docs/v5/concepts/themes/
  root.setThemes([
    am5themes_Animated.new(root)
  ]);

  const graficas = {
    "1": {
      "nombre": "/grafica_dinamica1",
      "valueField": "total_egresados",
      "categoryField": "ciudad"
    },
    "2": {
        "nombre": "/grafica_dinamica2",
        "valueField": "total_egresados",
        "categoryField": "nivel_educativo"
    }
  }

  fetchAndSetGrafica(graficas["1"].nombre, root, graficas["1"].valueField, graficas["1"].categoryField);

  const chartSelect = document.getElementById("chartSelect");
  chartSelect.addEventListener("change", async (e) => {
    const value = chartSelect.value;
    const grafica = graficas[value];
    fetchAndSetGrafica(grafica.nombre, root, grafica.valueField, grafica.categoryField);
  });


// Grafica2 ---------------------------------------------------------------------------------------


var root2 = am5.Root.new("chartdiv2");


// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root2.setThemes([
  am5themes_Animated.new(root2)
]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/xy-chart/
var chart = root2.container.children.push(am5xy.XYChart.new(root2, {
  panX: true,
  panY: true,
  wheelX: "panX",
  wheelY: "zoomX",
  pinchZoomX: true
}));

// Add cursor
// https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
var cursor = chart.set("cursor", am5xy.XYCursor.new(root2, {}));
cursor.lineY.set("visible", false);


// Create axes
// https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
var xRenderer = am5xy.AxisRendererX.new(root2, { minGridDistance: 30 });
xRenderer.labels.template.setAll({
  rotation: -90,
  centerY: am5.p50,
  centerX: am5.p100,
  paddingRight: 15,
  visible: false
});

xRenderer.grid.template.setAll({
  location: 1
})

var xAxis = chart.xAxes.push(am5xy.CategoryAxis.new(root2, {
  maxDeviation: 0.3,
  categoryField: "nivel_educativo",
  renderer: xRenderer,
  tooltip: am5.Tooltip.new(root2, {})
}));

var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root2, {
  maxDeviation: 0.3,
  renderer: am5xy.AxisRendererY.new(root2, {
    strokeOpacity: 0.1
  })
}));


// Create series
// https://www.amcharts.com/docs/v5/charts/xy-chart/series/
var series = chart.series.push(am5xy.ColumnSeries.new(root2, {
  name: "Series 1",
  xAxis: xAxis,
  yAxis: yAxis,
  valueYField: "salario_promedio",
  sequencedInterpolation: true,
  categoryXField: "nivel_educativo",
  tooltip: am5.Tooltip.new(root2, {
    labelText: "{valueY}"
  })
}));

series.columns.template.setAll({ cornerRadiusTL: 5, cornerRadiusTR: 5, strokeOpacity: 0 });
series.columns.template.adapters.add("fill", function(fill, target) {
  return chart.get("colors").getIndex(series.columns.indexOf(target));
});

series.columns.template.adapters.add("stroke", function(stroke, target) {
  return chart.get("colors").getIndex(series.columns.indexOf(target));
});


fetch("/grafica_dinamica3")
    .then(response => response.json())
    .then(data => {
      xAxis.data.setAll(data);
      series.data.setAll(data);
      console.log(data);
    })
    .catch(error => console.error("Error al obtener los datos:", error));

series.labels.template.setAll({
    visible: false,
  });
// Make stuff animate on load
// https://www.amcharts.com/docs/v5/concepts/animations/
series.appear(1000);
chart.appear(1000, 100);

// Grafica3 ---------------------------------------------------------------------------------------

}); // end am5.ready()
