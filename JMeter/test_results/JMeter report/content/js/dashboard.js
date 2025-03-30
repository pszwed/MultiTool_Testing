/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 91.66398972052683, "KoPercent": 8.336010279473177};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.2053958567528505, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.14, 500, 1500, "TC01 - POST /api/SecurityAnswers/"], "isController": false}, {"data": [0.012733446519524618, 500, 1500, "TC03 - POST /api/BasketItems/"], "isController": false}, {"data": [0.06174334140435835, 500, 1500, "TC02 - POST /rest/user/login"], "isController": false}, {"data": [0.0, 500, 1500, "TC11 - GET /rest/saveLoginIp"], "isController": false}, {"data": [1.0, 500, 1500, "OS Process Sampler - Windows"], "isController": false}, {"data": [1.0, 500, 1500, "Windows"], "isController": true}, {"data": [0.013043478260869565, 500, 1500, "TC07 - GET /api/Deliverys"], "isController": false}, {"data": [0.995, 500, 1500, "TC01 - GET /rest/admin/application-configuration"], "isController": false}, {"data": [0.010416666666666666, 500, 1500, "TC08 - GET /api/Cards"], "isController": false}, {"data": [0.002793296089385475, 500, 1500, "TC06 - POST /api/Addresss/"], "isController": false}, {"data": [1.0, 500, 1500, "TC02 - GET /rest/admin/application-configuration"], "isController": false}, {"data": [0.0, 500, 1500, "TC09 - POST /rest/basket/checkout"], "isController": false}, {"data": [0.04866180048661801, 500, 1500, "TC02 - GET /rest/products/search?q="], "isController": false}, {"data": [1.0, 500, 1500, "TC09 - GET /rest/track-order/"], "isController": false}, {"data": [0.195, 500, 1500, "TC01 - GET /api/SecurityQuestions/"], "isController": false}, {"data": [0.14, 500, 1500, "TC01 - POST /api/Users/"], "isController": false}, {"data": [0.02540106951871658, 500, 1500, "TC04 - GET /rest/basket"], "isController": false}, {"data": [0.005449591280653951, 500, 1500, "TC05 - DELETE /api/BasketItems"], "isController": false}, {"data": [0.0, 500, 1500, "TC08 - POST /api/Cards/"], "isController": false}, {"data": [1.0, 500, 1500, "TC02 - GET /api/Quantitys/"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 6226, 519, 8.336010279473177, 3840.064728557665, 5, 16897, 3469.0, 7690.800000000001, 8890.24999999999, 12861.649999999998, 20.490440975616178, 28.601727981044863, 30.27774422389904], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["TC01 - POST /api/SecurityAnswers/", 100, 0, 0.0, 4041.45, 163, 8784, 4231.0, 7778.6, 8385.249999999998, 8783.22, 1.319278618451431, 0.8395585075330808, 1.213929582679191], "isController": false}, {"data": ["TC03 - POST /api/BasketItems/", 1178, 338, 28.69269949066214, 5112.029711375221, 298, 10769, 5137.5, 7757.3, 8240.05, 9939.500000000002, 3.9933692442769053, 2.096691661595856, 6.617831512361478], "isController": false}, {"data": ["TC02 - POST /rest/user/login", 413, 0, 0.0, 2462.423728813559, 81, 4168, 2548.0, 3313.6000000000004, 3541.1999999999994, 3843.78, 1.3995635259512287, 1.6335411392887642, 1.2695822139790303], "isController": false}, {"data": ["TC11 - GET /rest/saveLoginIp", 323, 0, 0.0, 4509.1145510835895, 1675, 10293, 4585.0, 7038.600000000002, 8017.2, 10243.72, 1.1916049036570833, 0.8158598335534544, 1.873631112739474], "isController": false}, {"data": ["OS Process Sampler - Windows", 1, 0, 0.0, 361.0, 361, 361, 361.0, 361.0, 361.0, 361.0, 2.770083102493075, 0.03787222991689751, 0.0], "isController": false}, {"data": ["Windows", 1, 0, 0.0, 361.0, 361, 361, 361.0, 361.0, 361.0, 361.0, 2.770083102493075, 0.03787222991689751, 0.0], "isController": true}, {"data": ["TC07 - GET /api/Deliverys", 345, 0, 0.0, 3733.68985507246, 746, 8072, 3566.0, 5623.6, 6095.9, 7507.120000000002, 1.221905038498863, 0.7445983828352447, 1.917742050091023], "isController": false}, {"data": ["TC01 - GET /rest/admin/application-configuration", 100, 0, 0.0, 49.73, 19, 525, 33.0, 78.0, 133.34999999999985, 522.6999999999988, 1.6952025767079166, 14.637676936768944, 1.3343098406509577], "isController": false}, {"data": ["TC08 - GET /api/Cards", 336, 0, 0.0, 3368.9107142857147, 979, 7568, 2810.0, 5421.6, 5716.049999999998, 7107.08, 1.2097645279758047, 0.7122042816573053, 1.8939630477244904], "isController": false}, {"data": ["TC06 - POST /api/Addresss/", 358, 0, 0.0, 5866.117318435754, 1278, 11546, 5589.5, 8097.400000000001, 8523.7, 10263.250000000016, 1.2501877027626354, 0.7919255946248912, 2.184349976602632], "isController": false}, {"data": ["TC02 - GET /rest/admin/application-configuration", 313, 0, 0.0, 42.670926517571885, 17, 270, 35.0, 77.0, 97.60000000000002, 189.60000000000014, 1.1864644496586547, 10.244842445197092, 0.9338772914305424], "isController": false}, {"data": ["TC09 - POST /rest/basket/checkout", 334, 0, 0.0, 10030.832335329342, 3198, 16897, 9974.5, 13473.5, 14204.25, 16564.199999999993, 1.200868652294594, 0.4702620405958322, 2.0817453583190715], "isController": false}, {"data": ["TC02 - GET /rest/products/search?q=", 411, 0, 0.0, 2462.647201946473, 190, 4248, 2533.0, 3246.0, 3477.0, 4054.079999999999, 1.3916635627941625, 5.752843614558291, 2.11914360101412], "isController": false}, {"data": ["TC09 - GET /rest/track-order/", 325, 0, 0.0, 26.726153846153853, 17, 109, 23.0, 39.400000000000034, 54.099999999999966, 85.22000000000003, 1.2051856356705282, 0.9415476565165314, 1.9208877327862408], "isController": false}, {"data": ["TC01 - GET /api/SecurityQuestions/", 100, 0, 0.0, 2816.5800000000017, 109, 6018, 2876.5, 4936.6, 5135.7, 6013.499999999998, 1.550964700043427, 1.2722757305043737, 1.199574260189838], "isController": false}, {"data": ["TC01 - POST /api/Users/", 100, 0, 0.0, 3947.4900000000007, 137, 8796, 3647.0, 7469.900000000001, 8407.75, 8795.15, 1.4326852820240978, 1.0120858196392497, 1.6298474011088984], "isController": false}, {"data": ["TC04 - GET /rest/basket", 374, 0, 0.0, 3714.481283422459, 371, 7547, 3634.5, 5742.5, 6457.0, 7175.0, 1.2819106638514903, 1.2874034764543174, 1.9406063411733252], "isController": false}, {"data": ["TC05 - DELETE /api/BasketItems", 367, 181, 49.31880108991825, 5609.0653950953665, 1236, 13979, 5218.0, 9765.8, 10613.199999999999, 12930.999999999996, 1.2665785468513273, 0.4847609915377368, 2.021696736403262], "isController": false}, {"data": ["TC08 - POST /api/Cards/", 337, 0, 0.0, 5848.281899109791, 1909, 10949, 5529.0, 8033.399999999999, 8806.499999999998, 10613.86, 1.198111463473599, 0.6887210537870276, 2.01261602816273], "isController": false}, {"data": ["TC02 - GET /api/Quantitys/", 411, 0, 0.0, 9.0316301703163, 5, 90, 7.0, 16.0, 21.0, 40.639999999999986, 1.4016396797031663, 0.5393027673857885, 2.124753125127887], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["400/Bad Request", 304, 58.57418111753372, 4.882749759074847], "isController": false}, {"data": ["500/Internal Server Error", 34, 6.551059730250482, 0.5460970125281079], "isController": false}, {"data": ["404/Not Found", 181, 34.8747591522158, 2.9071635078702216], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 6226, 519, "400/Bad Request", 304, "404/Not Found", 181, "500/Internal Server Error", 34, "", "", "", ""], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": ["TC03 - POST /api/BasketItems/", 1178, 338, "400/Bad Request", 304, "500/Internal Server Error", 34, "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["TC05 - DELETE /api/BasketItems", 367, 181, "404/Not Found", 181, "", "", "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
