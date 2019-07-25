//const names = ['Alice', 'Bob', 'Charlie', 'Deborah', 'Evan'];

//for (let i = 0, i < 5, i++) {
  //console.log(names[i])
//}

//names.forEach((name) => {
  //console.log(name);
//}

let sum = 0;
let numbers = [0,1,2,3,4,5,6,7,8,9,10];

const findTotal = ((item) => {
  sum = sum + item;
})

numbers.forEach(findTotal);


const buttons = document.querySelectorAll('button');
const box = document.querySelector('#box');

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const color = button.innerHTML;
    box.style.background = color;
  });
});
