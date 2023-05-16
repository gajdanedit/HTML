console.log("Hello Világ");

function egy(f,c)
{
    c = (f-32)*5/9;
    return c;
}
var c = 0;
var f = 10;

function ketto(szam, szazalek)
{
    ertek = szam * (szazalek * 0.01);
    console.log(ertek);
}

function harom(a, b, c)
{
    if(a + b > c && b + c > a && a + c > b)
    {
        console.log("true")
    }
    else {
        console.log("false")
    }
}

function negy(a, b)
{
if(b % a == 0)
{
    console.log("True")
}
else{
    console.log("False")
}
}

function ot(a, b){
    if(a % b === 0){
        return true;
    } else {
        return false;
    }
}

var szamA = 10;
var szamB = 5;
var eredmeny = ot(szamA, szamB);
console.log("A(z)" + szamB + "osztója-e a(z)" + szamA + "-nak?" + eredmeny);

function hat(a, b)
{
    if(a > 0 && b > 0)
    {
        return "1. síknegyed";
    } else if (a < 0 && b > 0){
        return "2. síknegyed";
    } else if (a < 0 && b < 0){
        return "3. síknegyed";
    } else if(a > 0 && b < 0) {
        return "3. síknegyed"
    } else {
        return "Középpont vagy tengelyen van";
    }
}

function het(a, b) {
    if (a < b) {
        let temp = a;
        a = b;
        b = temp;
    }

    let maradek = a % b;
    while (maradek > 0) {
        a = b;
        b = maradek;
        maradek = a % b;
    }

    return b;
}

console.log(het(12, 18));  
console.log(het(15, 25));  
console.log(het(7, 5));    


function nyolc(a, b) {
    let x = a;
    let y = b;

    while (x !== y) {
        if (x < y) {
            x += a;
        } else {
            y += b;
        }
    }

    return x;
}
console.log(nyolc(3, 4)); 
console.log(nyolc(5, 7)); 
console.log(nyolc(6, 8)); 

function kilenc(n){
    if(n === 0 || n === 1) {
        return 1;
    } else {
      var a = n * kilenc (n - 1);
       return a;
    }
}
console.log(kilenc(6))


function tiz(a, b) {
    while (a >= b) {
        a -= b;
    }
    return a;
}
console.log(tiz(10, 3));   
console.log(tiz(17, 5));   
console.log(tiz(8, 4));  


function tizenegy(sorozat){
    for(var i = 0; i < sorozat.length; i ++){
        if(sorozat[i] < 0) {
            return sorozat[i];
        }
    }
    return null;
}

var szamsorozat = [1, 2, -3, 4, -5, 6];
var eredmeny = tizenegy(szamsorozat);


function tizenketto(tomb){
    var parosok = 0;
    for (var i = 0; i < tomb.length; i++) {
        if (tomb[i] % 2 === 0) {
            parosok++;
        }
    }
    return parosok;
}

var szamok = [1, 2, 3, 4, 5, 6];
var eredmeny = tizenketto(szamok);
console.log("A tömbben" + eredmeny + "db páros szám van.");

function tizenharom(tomb, ertek){
    var eredmeny = [];
    for (var i = 1; i < tomb.length - 1; i++){
        if(Math.abs(tomb[1] - tomb[i-1]) <= ertek && Math.abs(tomb[i] - tomb[i+1]) <= ertek){
            eredmeny.push(tomb[i]);
        }
    }
    return eredmeny;
}
var szamok = [2, 4, 7, 9, 8, 6, 5, 4, 3, 5];
var elteres = 1;
var eredmeny = tizenharom(szamok, elteres);


function tizennegy(tomb, reszszoveg, kezdo) {
    let eredmeny = [];

    for (let i = 0; i < tomb.length; i++) {
        if (tomb[i].includes(reszszoveg) && tomb[i].startsWith(kezdo)) {
            eredmeny.push(tomb[i]);
        }
    }

    return eredmeny;
}
let nevek = ["Anna", "Bence", "Cecília", "Dóra", "Erik", "Fanni"];
let reszszoveg = "ce";
let kezdo = "C";
console.log(tizennegy(nevek, reszszoveg, kezdo));  

let masikNevek = ["Adam", "Eva", "Istvan", "Imre", "Etelka", "Ildiko"];
let masikReszszoveg = "i";
let masikKezdo = "I";
console.log(tizennegy(masikNevek, masikReszszoveg, masikKezdo));


function tizenot(szam) {
    let faktorok = [];
    let oszto = 2;

    while (oszto <= szam) {
        if (szam % oszto === 0) {
            faktorok.push(oszto);
            szam /= oszto;
        } else {
            oszto++;
        }
    }

    return faktorok;
}
let szam = 84;
console.log(tizenot(szam)); 

let masikSzam = 120;
console.log(tizenot(masikSzam)); 


function tizenhat(matrix) {
    for (let i = 0; i < matrix.length; i++) {
      for (let j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] % 2 !== 0) {
          return false;
        }
      }
    }
    return true;
  }
  let matrix1 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
  ];
  console.log(tizenhat(matrix1));  
  
  let matrix2 = [
    [2, 4, 6],
    [8, 9, 12],
    [14, 16, 18]
  ];
  console.log(tizenhat(matrix2));  

  function tizenhet(matrix){
    var sorokSzama = matrix.length;
    var nemNullaSorok = 0;

    for (var i = 0; i < sorokSzama; i++) {
        var sor = matrix[i];
        var sorHossz = sor.length;
        var tartalmazNullat = false;

        for (var j = 0; j < sorHossz; j++){
            if (sor[j] === 0) {
                tartalmazNullat = true;
                break;
            }
        }
        if(!tartalmazNullat){
            nemNullaSorok++;
        }
    }
    return nemNullaSorok;
  }
  var matrix = [
    [1, 2, 3]
    [0, 4, 5]
    [6, 7, 8]
  ];

  var eredmeny = tizenhat(matrix);
  console.log("A mátrixban" + eredmeny + "db olyan sor van, amely nem tartalmaz 0 értéket.");




  function tizenhet(matrix) {
    let count = 0;
  
    for (let i = 0; i < matrix.length; i++) {
      let row = matrix[i];
      let containsZero = false;
  
      for (let j = 0; j < row.length; j++) {
        if (row[j] === 0) {
          containsZero = true;
          break;
        }
      }
  
      if (!containsZero) {
        count++;
      }
    } 
    return count;
  }
    let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8],
    [9, 0, 10]
  ];
  console.log(tizenhet(matrix)); 



  function tizennyolc(matrix) {
    let negativak = [];
  
    for (let i = 0; i < matrix.length; i++) {
      let row = matrix[i];
  
      for (let j = 0; j < row.length; j++) {
        if (row[j] < 0) {
          negativak.push(row[j]);
        }
      }
    }
  
    return negativak;
  }
  let matrix = [
    [1, -2, 3],
    [-4, 5, -6],
    [0, 7, -8],
    [-9, 0, 10]
  ];
  console.log(tizennyolc(matrix)); 

