var card = $("#card");

$(".btn-login").click(function(){
    card.css("transform", "rotateY(-180deg)");
});

$(".btn-register").click(function(){
    card.css("transform","rotateY(0deg)");
});