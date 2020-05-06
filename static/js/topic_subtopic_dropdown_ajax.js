$(document).ready(function () {
    console.log('document loaded')
    //make sure the document is loaded before running any javescript
    //update the subtopic field just in case there is a pre-filled topic

    //this is the AJAX part for the dropdown menu for topics and subtopics
    $("#topic").change(function () {
      var url = $("#main_form").attr("ajax_url");  // set the url of the `load_subtopics` view
      var topicId = $(this).val();  // get the selected topic from the HTML field
      var previous_topic = $('#previous_topic').val(); //get the previous topic fromt the HTML field
      var previous_subtopic = $('#previous_subtopic').val(); //get the previous subtopic from the HTML field

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request
        data: {
          'topic': topicId,       // add the topic to the GET parameters ,  this will be referenced to the views.py function
          'previous_topic': previous_topic, //add the previous topic to the GET parameters, this will be referenced to the views.py module
          'previous_subtopic': previous_subtopic, //add the previous subtopic to the GET parameters, this will be referenced to the views.py module
        },
        success: function (data) {   // `data` is the return of the `load_subtopics` view function
          $("#subtopic").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });
    });







});
