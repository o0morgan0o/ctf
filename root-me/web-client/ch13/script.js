
function dechiffre(pass_enc) {
    var pass = "70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65";
    var tab = pass_enc.split(',');
    var tab2 = pass.split(',');
    var i, j, k, o, p = ""; i = 0; j = tab.length;
    k = j;
    for (i = (o = 0); i < (k = j = tab2.length); i++) {
        o = tab[i]; p += String.fromCharCode((o = tab2[i]));
        if (i == 5) break;
    }
    for (i = (o = 0); i < (k = j = tab2.length); i++) {
        o = tab[i];
        if (i > 5 && i < k - 1)
            p += String.fromCharCode((o = tab2[i]));
    }
    p += String.fromCharCode(tab2[17]);
    return p
}
let test = String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));


// h = window.prompt('Entrez le mot de passe / Enter password');
let in1 = "test"
let in2 = "HAHA"
let tmp = dechiffre("FAUX PASSWORD HAHA")
let tmp_2 = dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30")
console.log('test', tmp);



// dechiffre('test')