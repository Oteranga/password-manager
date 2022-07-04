
var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
	overlay = document.getElementById('overlay'),
	overlay2 = document.getElementById('overlay2'),
	popup = document.getElementById('popup'),
	popup2 = document.getElementById('popup2'),
	btnCerrarPopup = document.getElementById('btn-cerrar-popup');
	btnCerrarPopup2 = document.getElementById('btn-cerrar-popup2');


    var table = document.getElementById("tableId");
    var rows = table.getElementsByTagName("tr");
    for (i = 0; i < rows.length; i++) {
      var currentRow = table.rows[i];
      var createClickHandler = function(row) {
        return function() {
            overlay.classList.add('active');
            popup.classList.add('active');
            console.log(this.id);
            document.getElementById('mpsw_id').value = this.id;

            /*

            var cell = row.getElementsByTagName("td")[0];
          var id = cell.innerHTML;
          alert("id:" + id);
          */
        };
      };
      currentRow.onclick = createClickHandler(currentRow);
    }

btnCerrarPopup.addEventListener('click', function(e){
    console.log("cerrar");
	e.preventDefault();
	popup.classList.remove('active');

    overlay.classList.remove('active');
});

btnCerrarPopup2.addEventListener('click', function(e){
  console.log("cerrar");
e.preventDefault();
popup2.classList.add('hidden');

  overlay2.classList.add('hidden');
});