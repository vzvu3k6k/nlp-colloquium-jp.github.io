$(document).ready(function(){
    const entries = window.performance.getEntriesByType('navigation')
    var isBrowserBackUsed = false;
    var isExpandedPrev = sessionStorage.getItem('isExpanded');

    for (const entry of entries) {
        if (entry.type === 'back_forward' | entry.type === 'reload') {
            isBrowserBackUsed = true;
        }
    }

    if (!isBrowserBackUsed | !isExpandedPrev) {
        console.log("!");
        $(".hidden-row").hide();
        $(".expand-button-row").show();
        sessionStorage.setItem('isExpanded', false);
    };

    $("#show-more-btn").click(function(){
        $(".hidden-row").show();
        $(this).hide();
        $(".expand-button-row").hide();
        sessionStorage.setItem('isExpanded', true);
    });
});