var Billboard = {};


Billboard.init = function(){
  $(document).ready(function(){
      $(".postBox").hide();
        $("#addMsg").click(function () {
             $(".postBox").css('display', 'inline-block')
        });
      
      $(".xBtn").click(function () {
          $(".postBox").hide();
          $(".postBox input").each(function(){
             $(this).val("");
          });
      })
  });
    
};

Billboard.init();

