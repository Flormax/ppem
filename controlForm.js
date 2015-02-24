document.forms[0].addEventListener('submit', function(event) {
	var envoi;
	var inputs = document.getElementsByTagName("input");
	var erreurInput;

	function getErreur(element) {
		while (element = element.nextSibling) {
			if (element.className === 'erreur') return element;	
		}
		return false;
	}

	function verifEmail(email) {
		var reg = new RegExp('^[a-z0-9]+([_|\.|-]{1}[a-z0-9]+)*@[a-z0-9]+([_|\.|-]{1}[a-z0-9]+)*[\.]{1}[a-z]{2,6}$', 'i');

		if(reg.test(email))	{
			return(true);
		}
		else	{
			return(false);
		}
	}

	for(var i = 0 ; i < inputs.length ; i++){
		erreurInput = getErreur(inputs[i]);

		if (inputs[i].getAttribute("type") == "email") {
			if (inputs[i].value == "" || (!verifEmail(inputs[i].value))) {
				erreurInput.style.display = 'block';
				erreurInput.innerHTML = "Veuillez saisir une adresse courriel valide.";
				envoi = event.preventDefault();
			}
			else {
				erreurInput.style.display = 'none';
				erreurInput.innerHTML = "";

				if (inputs[i].getAttribute("id") == "emailApr") {
					if (document.getElementById("emailAvt").value != inputs[i].value) {
						erreurInput.style.display = 'block';
						erreurInput.innerHTML = "Les emails ne correspondent pas.";
						envoi = event.preventDefault();
					}
					else {
						erreurInput.style.display = 'none';
						erreurInput.innerHTML = "";
					}
				}
			}
		}

		if (inputs[i].getAttribute("type") == "password" || inputs[i].getAttribute("type") == "text") {
			if (inputs[i].value == "") {
				erreurInput.style.display = 'block';
				erreurInput.innerHTML = "Veuillez remplir ce champ.";
				envoi = event.preventDefault();
			}
			else {
				erreurInput.style.display = 'none';
				erreurInput.innerHTML = "";

				if (inputs[i].getAttribute("id") == "mdpApr") {
					if (document.getElementById("mdpAvt").value != inputs[i].value) {
						erreurInput.style.display = 'block';
						erreurInput.innerHTML = "Les mots de passe ne correspondent pas.";
						envoi = event.preventDefault();
					}
					else {
						erreurInput.style.display = 'none';
						erreurInput.innerHTML = "";
					}
				}
			}
		}
	}
	
   	return envoi;

}, true);