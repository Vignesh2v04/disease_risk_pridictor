const btn =document.getElementsByClassName('toggle-button')
const p=document.querySelector('p');
function toggleMenu() { 
    const menu = document.querySelector('.menu'); 
    menu.classList.toggle('active'); 
    btn.namedItem='×';
  }
  function toggleMode()
{
  var ele=document.body;
 ele.classList.toggle('bright-mode');
 ele.classList.toggle('clorchange')

}
function openPredictPage(){
    window.location.href='/prediction'
}s