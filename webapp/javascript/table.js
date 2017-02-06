$.ajax({
    type: "GET",
    url: "data/table.csv",
    dataType: "text",
    success: function(data) {makeTable(data);}
});

function makeTable(csv) {

    var rows = csv.split('\n'),
    table = document.createElement('table');
    table.className = "table table-hover";


    // add table header
    thead = document.createElement('thead');
    tr = document.createElement('tr');
    ths = rows[0].split(',');
    for (var i=0; i<ths.length; i++) {
        td = document.createElement('th');
        td.innerHTML = ths[i];
        tr.appendChild(td);
    }
    thead.appendChild(tr);
    table.appendChild(thead);

    // add table body
    tbody = document.createElement('tbody');
    for ( var i = 1; i < rows.length; i++ ) {
        tr = document.createElement('tr');
        tds = rows[i].split(',');
        th = document.createElement('th');
        th.scope = "row";
        th.innerHTML = tds[0];
        tr.appendChild(th);
        for ( var j = 1; j < tds.length; j++ ) {
            td = document.createElement('td');
            td.innerHTML = tds[j];
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    table.appendChild(tbody);

    // add table to body of the document
    body = document.getElementsByTagName("body")[0];
    body.appendChild(table);
}
