/*$(document).ready(function(){
    $(".decrement_btn").click(function(){
        if(Number($(this).next().text()) >0){
            $(this).next().text(Number($(this).next().text()) -1);
        }
    });
    $(".increment_btn").click(function(){
            $(this).prev().text(Number($(this).prev().text()) +1);
    });

$(".reset").click(function(){
    $("span").each(function(){
        $(this).text(0);
    });
});

$(">book_now").click(function(){
    $(".under_4_list").text(Number($(".under_4").text())*5);
    $(".children_list").text(Number($(".children").text())*10);
    $(".adults_list").text(Number($(".adults").text())*15);

    $(".total").text(Number($(".under_4_list").text()) + (Number($(".children_list").text()) + (Number($(".adults_list").text());
    $(".quantity_under_4").text($(".under_4").text());
    $(".quantity_children").text($(".children").text());
    $(".quantity_adults").text($(".adults").text());




});

});

var x = 0;

document.getElementsByClassName('btn btn-outline-primary decrement_btn').innerHTML = x;

function button1() {
  document.getElementsByClassName('fas fa-plus').innerHTML = ++x;
}

function button2() {
  document.getElementsByClassName('fas fa-minus ').innerHTML = --x;
}

var number = x;*/

const decrementButton = document.querySelector('.decrement_btn');
    const incrementButton = document.querySelector('.increment_btn');
    const display = document.querySelector('.children');

    let count = 0;

    decrementButton.addEventListener('click', () => {
        count--;
        display.textContent = count;
    });

    incrementButton.addEventListener('click', () => {
        count++;
        display.textContent = count;
    });
