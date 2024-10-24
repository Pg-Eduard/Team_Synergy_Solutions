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

function api_vreme() { //nou
    fetch("/api_vreme")
    .then(response => response.json())
    .then(data => {
        const parsedData = JSON.parse(data.data);

        document.getElementById("temp_min").textContent = "Temperatura minima: " + parsedData.temp_min + "oC";
        document.getElementById("temp_max").textContent = "Temperatura maxima: " + parsedData.temp_max + "oC";
        document.getElementById("feelslike").textContent = "Se simte ca si: " + parsedData.feelslike + "oC";
        document.getElementById("humidity").textContent = "Umiditatea: " + parsedData.humidity + "%";
        document.getElementById("sunrise").textContent = "Rasaritul se va petrece la ora: " + parsedData.sunrise;
        document.getElementById("sunset").textContent = "Apusul se va petrece la ora: " + parsedData.sunset;
        document.getElementById("description_wheather").textContent = "Descrierea vremii: " + parsedData.icon;
    })
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

function toggleVent(){
	fetch("/vent")
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

document.getElementById('form_logare').addEventListener('submit', handleLogin);
document.getElementById('form_signUp').addEventListener("submit", handleSignUp);

function switchSignUp() {
    login = document.getElementById("login_box");
    signup = document.getElementById("signUp_box");
    signup.hidden = false;
    login.hidden = true;
}

function switchLogIn() {
    signup = document.getElementById("signUp_box");
    login = document.getElementById("login_box");
    signup.hidden = true;
    login.hidden = false;
}

function check_avalability(){
    fetch("check_avalability")
    .then(response => response.json())
    .then(data => {
        if(data.over_limit){
            document.getElementById("login_to_signup").disabled = true;
        }
    })
}

function handleSignUp(event) {
    event.preventDefault();  // Previne trimiterea normala a formularului

    // Preluam valorile introduse
    const username = document.getElementById('username_sign').value;
    const password = document.getElementById('pass_sign').value;

    // Trimiterea datelor catre Flask prin AJAX (format JSON)
    fetch('/save_users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Specificam explicit ca trimitem date ï¿½n format JSON
        },
        body: JSON.stringify({ username_sign: username, password_sign: password })  // Convertim datele ï¿½n format JSON
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            //window.location.href = '/home';  // Redirec?ionam la pagina de home daca autentificarea a reu?it
            //test();
            switchLogIn();
        }
        else{
            document.getElementById("errorMessage_sign").textContent = data.message;
            if(data.field === "username_sign"){
                document.getElementById("username_sign").classList.add("is-invalid");
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function handleLogin(event) {
    event.preventDefault();  // Previne trimiterea normala a formularului

    // Preluam valorile introduse
    const username = document.getElementById('username').value;
    const password = document.getElementById('pass').value;

    // Resetam mesajele de eroare ?i borderele ro?ii
    document.getElementById('errorMessage').textContent = '';
    document.getElementById('username').classList.remove('is-invalid');
    document.getElementById('pass').classList.remove('is-invalid');

    // Trimiterea datelor catre Flask prin AJAX (format JSON)
    fetch('/logare', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Specificam explicit ca trimitem date ï¿½n format JSON
        },
        body: JSON.stringify({ username: username, password: password })  // Convertim datele ï¿½n format JSON
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/ro';  // Redirec?ionam la pagina de home daca autentificarea a reu?it
            //test();
        } else {
            // Afi?am mesajul de eroare ?i punem bordere ro?ii
            document.getElementById('errorMessage').textContent = data.message;
            if (data.field === 'username') {
                document.getElementById('username').classList.add('is-invalid');
            } else if (data.field === 'pass') {
                document.getElementById('pass').classList.add('is-invalid');
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}