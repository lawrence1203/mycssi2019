const myButton = document.querySelector('#mybutton');
const myBox = document.querySelector('#box');
myButton.addEventListener('click', (event) => {
  console.log('Like Button Clicked!');
  myButton.innerHTML = 'get fucked!';
});

myButton.addEventListener('click', (event) => {
  myBox.style.innerHTML('sigma balls')
  myBox.style.backgroundImage = "url(https://i0.wp.com/media.criticalhit.net//2019/07/sigma-origin-cropped-hed-1180285-1280x0.jpg?w=850&ssl=1)"
});
