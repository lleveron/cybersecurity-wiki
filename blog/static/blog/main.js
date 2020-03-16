$( document ).ready(function() {

    //Navigation Bar Functions
    function opensidebar(){
        $("#sidebar").css("width","250px");
        $("#sidebar-links li").css("opacity","1");
        $("#sidebar-icons").stop().fadeOut();
    }

    function closesidebar(){
        $("#sidebar").css("width","100px");
        $("#sidebar-links li").css("opacity","0");
        $("#sidebar-icons").stop().fadeIn();
    }
    
    //AOS Config
    AOS.init({
        once: true,
        duration: 700,
    });
    
    //Side Bar Show/Hide
    $("#sidebar").hover(function(){
        opensidebar() 
    }, function (){
        closesidebar()
    })

    //Side Bar Hover Effects
    $("#sidebar-links li").hover(function(){
        $(this).css("background-color","rgba(226, 226, 226, 0.11)");
    }, function(){
        $(this).css("background-color","");
    })

    //User Settings Show/Hide
    $("#navbar-image").click(function(){
        $("#user-settings").slideToggle(300);
    })

    //Profile Section Button Effect
    $("#profile-btn").click(function(){
        $("#edit-profile").fadeToggle().toggleClass("*");
        if ($("#edit-profile").hasClass("*")){
            $("#profile-btn").text("Cancel");
        } else {
            $("#profile-btn").text("Edit");
        }
    })
    
});
