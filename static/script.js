const request_path = document.location.pathname

function getXMLDoc() {
    var req = new XMLHttpRequest();
    req.open('GET', request_path + '/random', true);
    req.onreadystatechange = function (aEvt) {
        if (req.readyState == 4) {
            if (req.status == 200) {
                document.getElementById("phrase-box").innerHTML = req.responseText;
            } else
                console.log("Błąd podczas ładowania strony\n");
        }
    };

req.send(null); }

window.addEventListener( "load", function () {
    getXMLDoc();
    } );

window.addEventListener('keyup', select_by_key);

function select_by_key(event) {
    if (event.isComposing || (event.keyCode === 97 || event.keyCode === 49 || event.keyCode === 74)) { // j,1,1
        const radio_btn_yes = document.getElementById("check_yes");
        radio_btn_yes.checked = true;
        const form = document.getElementById("check_intent_form");
        send_and_receive(form)
    }
}

function send_and_receive(form){
    const XHR = new XMLHttpRequest();
    const FD = new FormData( form );

    // Define what happens on successful data submission
    XHR.addEventListener( "load", function(event) {
      getXMLDoc();
    } );

    // Define what happens in case of error
    XHR.addEventListener( "error", function( event ) {
      alert( 'Oops! Something went wrong.' );
    } );
    XHR.open( "POST", request_path+"/update" );
    XHR.send( FD );
  }

  window.addEventListener( "change", function () {
      if (request_path == "/active_learning/check"){
          form = document.getElementById( "check_intent_form" );
          send_and_receive(form);
      }
      else if (request_path == "/active_learning/tag") {
        form = document.getElementById( "tag_intent_form" );
        send_and_receive(form);
      }
} );


