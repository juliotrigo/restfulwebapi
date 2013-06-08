var xmlHttp = null;

function SendHTTPRequest()
{
    xmlHttp = new XMLHttpRequest(); 
    xmlHttp.onreadystatechange = ProcessRequest;
    xmlHttp.open( "GET", "/", true );
    xmlHttp.send( null );
}