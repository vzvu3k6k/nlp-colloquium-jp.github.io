$(document).ready(function(){
    $(".hidden-row").hide();
    $(".expand-button-row").show();

    $("#show-more-btn").click(function(){
        $(".hidden-row").show();
        $(this).hide();
        $(".expand-button-row").hide();
    });
});