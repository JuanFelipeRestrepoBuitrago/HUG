// Función para cargar y actualizar el gráfico
  function updateChart(selectedValue) {
    var chartdiv = document.getElementById("chartdiv");
    chartdiv.innerHTML = "";

    // Cargar datos según la opción seleccionada
    var url = selectedValue === "1" ? "/grafica_dinamica1/" : "/grafica_dinamica2/";

    fetch(url)
      .then(response => response.json())
      .then(data => {
        // Crear el nuevo gráfico con los datos cargados
        am5.ready(function() {
          var root = am5.Root.new("chartdiv");
          root.setThemes([am5themes_Animated.new(root)]);
          var chart = root.container.children.push(am5percent.PieChart.new(root, {
            layout: root.verticalLayout
          }));
          var series = chart.series.push(am5percent.PieSeries.new(root, {
            valueField: "total_egresados",
            categoryField: selectedValue === "1" ? "ciudad" : "nivel_educativo",
            alignLabels: false
          }));
          series.data.setAll(data);
          series.labels.template.setAll({
            visible: false,
          });
          series.appear(1000, 100);
        });
      })
      .catch(error => console.error("Error al obtener los datos:", error));
  }

  // Detectar el cambio en el elemento select
  document.getElementById("chartSelect").addEventListener("change", function() {
    var selectedValue = this.value;
    updateChart(selectedValue);
  });

  // Inicializar el gráfico con la opción predeterminada
  updateChart(document.getElementById("chartSelect").value);