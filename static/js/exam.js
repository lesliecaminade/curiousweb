$(document).ready(function() {
  function copyToClipboard(text) {
      var $temp = $("<input>");
      $("body").append($temp);
      $temp.val(text).select();
      document.execCommand("copy");
      $temp.remove();
  }

  $(".nc").bind("contextmenu",function(e){
     return false;
   });

  $(document).keyup(function(e) {
      copyToClipboard(" ");
      console.log('activate')
  });
});
