function validateForm() {

    var erreurs = document.getElementsByClassName("erreur")
    for (let i = 0; i < erreurs.length; i++) {
        erreurs[i].innerHTML = ""
    }

    var nom = document.getElementById("nom").value;
    if (nom == "") {
        alert("Vous avez oublié de préciser votre nom");
        document.getElementById("nom_erreur").innerHTML = "* Champ obligatoire"
        return false;
    }

    var prenom = document.getElementById("prenom").value;
    if (prenom == "") {
        alert("Vous avez oublié de préciser votre prenom");
        document.getElementById("prenom_erreur").innerHTML = "* Champ obligatoire"
        return false;
    }

    var genre = document.getElementsByName("genre");
    if (!((genre[0].checked) || (genre[1].checked))) {
        alert("Vous avez oublié de préciser votre genre");
        document.getElementById("genre_erreur").innerHTML = "* Champ obligatoire"
        return false;
    }

    var spe1 = document.getElementById("spe1").value;
    if (spe1 == "") {
        alert("Vous avez oublié de préciser votre premiere specialié");
        document.getElementById("spe1_erreur").innerHTML = "* Champ obligatoire"
        return false;
    }

    var spe2 = document.getElementById("spe2").value;
    if (spe2 == "") {
        alert("Vous avez oublié de préciser votre deuxieme specialié");
        document.getElementById("spe2_erreur").innerHTML = "* Champ obligatoire"
        return false;
    }

    var spe3 = document.getElementById("spe3").value;
    if (spe3 == "") {
        alert("Vous avez oublié de préciser votre troisieme specialié");
        document.getElementById("spe3_erreur").innerHTML = "* Champ obligatoire"
        return false;
    }

    if ((spe1 == spe2) || (spe1 == spe3) || (spe2 == spe3)) {
        alert('vous ne pouvez pas prendre deux fois la meme spe')
        document.getElementById("spe1_erreur").innerHTML = "* doit etre different"
        return false
    }

    return true;
}