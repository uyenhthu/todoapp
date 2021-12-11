// ajax.js
// javascript code for json api example
//
// The idea here is that we use client-side javascript
// to fetch some data from the server, which supplies
// it in a json format. The flask code has a route,
// (e.g. /count_posts.json) which delivers a small
// chuck of data in json format (e.g. '{"posts": 5}').
//

function updateListcount(result){
    // Update the postcount DOM element defined in templates/base.html.
    // The input arg 'result' is a json object; in this case a dictionary,
    // as created in the postcount() function within blogapp.py
    // and loaded from within the init() function below.
    $('#ajaxlists').html(result['listcounts']);
}

function init(){
    // Access the postcount API to get the number of posts, in json format.
    $.ajax({
	url: '/listcount.json',
	type: 'GET',
	success: result => updateListcount(result),
	error: function(){window.alert("OOPS - ajax error.");}
    });
}

window.onload = init;  // run the init() script after the browser window loads
