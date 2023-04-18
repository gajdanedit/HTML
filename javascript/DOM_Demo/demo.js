console.dir(document);

console.log(document);
console.log(document.title);
document.title = "Welcome";
console.log(document.links);

console.log(document.links[0].innerText);
document.links[0].innerHTML  = "ELTE linkek";
document.links[1].style.color  = 'red';

console.log(document.getElementById("header-title"));
var header = document.getElementById("header-title");

header.style.backgroundColor = "gray";

var elemek = document.getElementsByTagName('li');
console.log(elemek);
console.log(elemek[0]);

elemek[0].InnerText = 'kalap';
elemek[1].style.color = 'blue';

