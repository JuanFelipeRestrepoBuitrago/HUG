am5.ready(function () {

            // https://www.amcharts.com/docs/v5/getting-started/#Root3_element
            var root3 = am5.Root.new("chartdiv3");


            var myTheme = am5.Theme.new(root3);

            myTheme.rule("Grid", ["base"]).setAll({
              strokeOpacity: 0.1
            });


            // Set themes
            // https://www.amcharts.com/docs/v5/concepts/themes/
            root3.setThemes([
              am5themes_Animated.new(root3),
              myTheme
            ]);


            // Create chart
            // https://www.amcharts.com/docs/v5/charts/xy-chart/
            var chart = root3.container.children.push(
              am5xy.XYChart.new(root3, {
                panX: false,
                panY: false,
                wheelX: "none",
                wheelY: "none"
              })
            );


            // Create axes
            // https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
            var yRenderer = am5xy.AxisRendererY.new(root3, { minGridDistance: 30 });
            yRenderer.grid.template.set("location", 1);

            var yAxis = chart.yAxes.push(
              am5xy.CategoryAxis.new(root3, {
                maxDeviation: 0,
                categoryField: "nivel_educativo",
                renderer: yRenderer
              })
            );

            var xAxis = chart.xAxes.push(
              am5xy.ValueAxis.new(root3, {
                maxDeviation: 0,
                min: 0,
                renderer: am5xy.AxisRendererX.new(root3, {
                  visible: true,
                  strokeOpacity: 0.1
                })
              })
            );


            // Create series
            // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
            var series = chart.series.push(
              am5xy.ColumnSeries.new(root3, {
                name: "Series 1",
                xAxis: xAxis,
                yAxis: yAxis,
                valueXField: "experiencia_promedio",
                sequencedInterpolation: true,
                categoryYField: "nivel_educativo"
              })
            );

            var columnTemplate = series.columns.template;

            columnTemplate.setAll({
              draggable: true,
              cursorOverStyle: "pointer",
              tooltipText: "arrastra para reubicar",
              cornerRadiusBR: 10,
              cornerRadiusTR: 10,
              strokeOpacity: 0
            });
            columnTemplate.adapters.add("fill", (fill, target) => {
              return chart.get("colors").getIndex(series.columns.indexOf(target));
            });

            columnTemplate.adapters.add("stroke", (stroke, target) => {
              return chart.get("colors").getIndex(series.columns.indexOf(target));
            });

            columnTemplate.events.on("dragstop", () => {
              sortCategoryAxis();
            });

            // Get series item by category
            function getSeriesItem(category) {
              for (var i = 0; i < series.dataItems.length; i++) {
                var dataItem = series.dataItems[i];
                if (dataItem.get("categoryY") == category) {
                  return dataItem;
                }
              }
            }


            // Axis sorting
            function sortCategoryAxis() {
              // Sort by value
              series.dataItems.sort(function(x, y) {
                return y.get("graphics").y() - x.get("graphics").y();
              });

              var easing = am5.ease.out(am5.ease.cubic);

              // Go through each axis item
              am5.array.each(yAxis.dataItems, function(dataItem) {
                // get corresponding series item
                var seriesDataItem = getSeriesItem(dataItem.get("category"));

                if (seriesDataItem) {
                  // get index of series data item
                  var index = series.dataItems.indexOf(seriesDataItem);

                  var column = seriesDataItem.get("graphics");

                  // position after sorting
                  var fy =
                    yRenderer.positionToCoordinate(yAxis.indexToPosition(index)) -
                    column.height() / 2;

                  // set index to be the same as series data item index
                  if (index != dataItem.get("index")) {
                    dataItem.set("index", index);

                    // current position
                    var x = column.x();
                    var y = column.y();

                    column.set("dy", -(fy - y));
                    column.set("dx", x);

                    column.animate({ key: "dy", to: 0, duration: 600, easing: easing });
                    column.animate({ key: "dx", to: 0, duration: 600, easing: easing });
                  } else {
                    column.animate({ key: "y", to: fy, duration: 600, easing: easing });
                    column.animate({ key: "x", to: 0, duration: 600, easing: easing });
                  }
                }
              });

              // Sort axis items by index.
              // This changes the order instantly, but as dx and dy is set and animated,
              // they keep in the same places and then animate to true positions.
              yAxis.dataItems.sort(function(x, y) {
                return x.get("index") - y.get("index");
              });
            }

            // Set data
            fetch("/grafica_dinamica4")
                .then(response => response.json())
                .then(data => {
                    yAxis.data.setAll(data);
                    series.data.setAll(data);
                    console.log(data);
                })
                .catch(error => console.error("Error al obtener los datos:", error));

            yAxis.data.setAll(data);
            series.data.setAll(data);


            // Make stuff animate on load
            // https://www.amcharts.com/docs/v5/concepts/animations/
            series.appear(1000);
            chart.appear(1000, 100);

}); // end am5.ready()