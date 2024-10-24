function afisareCi() {
	const ci = document.getElementById("control_inteligent");
	const info = document.getElementById("informatii");
	const sec = document.getElementById("securitate");

	ci.hidden = false;
	info.hidden = true;
	sec.hidden = true;
}

function afisareInfo() {
	const ci = document.getElementById("control_inteligent");
	const info = document.getElementById("informatii");
	const sec = document.getElementById("securitate");
	
	ci.hidden = true;
	info.hidden = false;
	sec.hidden = true;
}

function afisareSec() {
	const ci = document.getElementById("control_inteligent");
	const info = document.getElementById("informatii");
	const sec = document.getElementById("securitate");
	
	ci.hidden = true;
	info.hidden = true;
	sec.hidden = false;
}

function toggleLight(id) {
    // Use AJAX to call Flask route
    fetch(`/toggle_light/${id}`)
    .then(response => response.text())
    .then(data => {
        // Update button text or UI based on response (optional)
    })
}

function toggleGaraj(){
	fetch('/usa_garaj')
}

function toggleIntrare(){
	fetch("/usa_intrare")
}

function inlocuireSeismica() {
	fetch('/vibratii')
	.then(response => response.json())
	.then(data => {
		const parsedData = JSON.parse(data.data)

		document.getElementById("activitateS").textContent = "Ultima activitate detectata pe: " + parsedData.activitate;
	})
}

function inlocuireTemp() {
	fetch("/temp")
	.then(response => response.json())
	.then(data => {
		const parsedData = JSON.parse(data.data)

		if(parsedData.valid == "true"){
			document.getElementById("temp").textContent = "Temperatura in grade Celsius este: " + parsedData.temp_c;
			document.getElementById("umi").textContent = "Umiditatea este: " + parsedData.umi;
		}
		else{
			document.getElementById("temp").textContent = parsedData.rezultat;
			document.getElementById("umi").textContent = parsedData.rezultat;
		}
	})
}

function inlocuireText() {
	fetch('/get_text')
    .then(response => response.json())
    .then(data => {
      // Actualizeaza textul elementului cu id-ul "myElement" cu datele primit
	  const parsedData = JSON.parse(data.data);

      document.getElementById("ledBu").textContent = "Bucatarie: " + parsedData.ledBu;
	  document.getElementById("ledGa").textContent = "Garaj: " + parsedData.ledGa;
	  document.getElementById("ledBa").textContent = "Baie: " + parsedData.ledBa;
	  document.getElementById("ledDi").textContent = "Dining: " + parsedData.ledDi;
	  document.getElementById("ledIn").textContent = "Living: " + parsedData.ledIn;
	  document.getElementById("ledCa").textContent = "Camera: " + parsedData.ledCa;
    });
}

function inlocuireText_spaniola(){
	fetch('/get_text')
    .then(response => response.json())
    .then(data => {
      // Actualizeaza textul elementului cu id-ul "myElement" cu datele primit
	  const parsedData = JSON.parse(data.data);

	  var bu = parsedData.ledBu;
	  var ga = parsedData.ledGa;
	  var ba = parsedData.ledBa;
	  var di = parsedData.ledDi;
	  var intrare = parsedData.ledIn;
	  var ca = parsedData.ledCa;
	  var array = [bu,ga,ba,di,intrare,ca];
	  //if(bu == "Stins"){bu = "Apagado"} else if(bu == "Aprins"){bu = "encendido"}
	  for(i=0;i<=5;i++){
		if(array[i]=="Stins"){array[i] = "Apagado"} else if(array[i] == "Aprins"){array[i]="Encendido"}
	  }


      document.getElementById("ledBu").textContent = "Cocina: " + array[0];
	  document.getElementById("ledGa").textContent = "Garaje: " + array[1];
	  document.getElementById("ledBa").textContent = "Bano: " + array[2];
	  document.getElementById("ledDi").textContent = "Comedor: " + array[3];
	  document.getElementById("ledIn").textContent = "Entrada: " + array[4];
	  document.getElementById("ledCa").textContent = "Dormitorio: " + array[5];
    });
}

function inlocuireText_engleza(){
	fetch('/get_text')
    .then(response => response.json())
    .then(data => {
      // Actualizeaza textul elementului cu id-ul "myElement" cu datele primit
	  const parsedData = JSON.parse(data.data);

	  var bu = parsedData.ledBu;
	  var ga = parsedData.ledGa;
	  var ba = parsedData.ledBa;
	  var di = parsedData.ledDi;
	  var intrare = parsedData.ledIn;
	  var ca = parsedData.ledCa;
	  var array = [bu,ga,ba,di,intrare,ca];
	  //if(bu == "Stins"){bu = "Apagado"} else if(bu == "Aprins"){bu = "encendido"}
	  for(i=0;i<=5;i++){
		if(array[i]=="Stins"){array[i] = "Turned Off"} else if(array[i] == "Aprins"){array[i]="Turned On"}
	  }


      document.getElementById("ledBu").textContent = "Chicken: " + array[0];
	  document.getElementById("ledGa").textContent = "Garage: " + array[1];
	  document.getElementById("ledBa").textContent = "Bathroom: " + array[2];
	  document.getElementById("ledDi").textContent = "Dining: " + array[3];
	  document.getElementById("ledIn").textContent = "Entrance: " + array[4];
	  document.getElementById("ledCa").textContent = "Bedroom: " + array[5];
    });
}

function inlocuireDetectii() {
	fetch('get_detectii')
	.then(response => response.json())
	.then(data => {
		const parsedData = JSON.parse(data.data)

		document.getElementById("detectie1").textContent = parsedData.data1;
		document.getElementById("detectie2").textContent = parsedData.data2;
		document.getElementById("detectie3").textContent = parsedData.data3;
	})
}