let elemento;

elemento = document;
elemento = document.all;
elemento = document.head;
elemento = document.domain;                  //* Muestra Localhost
elemento = document.forms;                   //* Muestra los formularios
elemento = document.forms[0];
elemento = document.forms[0].id;
elemento = document.forms[0].method;
elemento = document.forms[0].classList;
elemento = document.forms[0].action;
elemento = document.links;
elemento = document.links[4];
elemento = document.links[4].classList;      //* Va como "objeto"
elemento = document.links[4].className;      //* Muestra como "string"

elemento = document.images;
elemento = document.scripts;

console.log(elemento);