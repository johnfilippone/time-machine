$.ajax({
    type: "GET",
    url: "data/time-machine.csv",
    dataType: "text",
    success: function(data) {makeTable(data);}
});

function makeTable(csv) {

    var rows = csv.split('\n'),
    table = document.createElement('table');
    table.className = "table table-hover";
    tr = null; 
    td = null;
    tds = null;

    for ( var i = 0; i < rows.length; i++ ) {
        tr = document.createElement('tr');
        tds = rows[i].split(',');
        for ( var j = 0; j < tds.length; j++ ) {
           td = document.createElement('td');
           td.innerHTML = tds[j];
           tr.appendChild(td);
        }
        table.appendChild(tr);
    }

    document.getElementsByTagName("body")[0].appendChild(table);
}

/*
    <table class="table table-hover">
      <thead>
        <tr>
          <th>#</th>
          <th>Activity</th>
          <th>Minutes</th></tr></thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td colspan="2">Larry the Bird</td>
        </tr>
      </tbody>
    </table>

*/
