//document.getElementById("product") se utiliza para recuperar el elemento con id="product"
const priceElement = document.getElementById("product");
const numberElement = document.getElementById("number");
let compra = [];

function add() {
  const price = parseInt(priceElement.value);
  const number = parseInt(numberElement.value);
  let compra = {
    price: price,
    number: number,
  };
  purchases.push(purchase);
}

function calc() {
  let sum = 0;
  let postage;
   for(let i=0; i<purchases.length; i++){
    sum += compra[i].price * compra[i].number;
  }
  if (sum == 0 || sum >= 3000) {
    postage = 0;
  } else if (sum < 1000){
    postage = 500;
  } else {
    postage = 250;
  }
  window.alert(`Los gastos de envío son.${postage}Yenes. Total.${sum + postage}Círculo.`)
  purchases = [];
  priceElement.value= "";
  numberElement.value = "";
