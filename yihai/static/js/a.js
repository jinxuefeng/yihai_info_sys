
xmlHttp = new XMLHttpRequest();


function log_out(){
    /*xmlHttp.onreadystatechange = handleStateChange;
    xmlHttp.open("GET", "/log_out/", true);
    xmlHttp.send(null)   
    */
    //page jump, this doesnt work:  window.navigate("/log_out/");
    self.location='/log_out/';
}

function getCousrse(){
    xmlHttp.onreadystatechange = handleStateChange;
    xmlHttp.open("GET", "/company/course_lst/", true);
    xmlHttp.send(null)
}

function handleStateChange(){
    if(xmlHttp.readyState == 4){
        if(xmlHttp.status == 200){
            var resp = xmlHttp.responseText;
            var jsn = eval(resp);
            var info_div = document.getElementById("info");
            var i=0;
            $("#info").empty();
            for(;i<jsn.length;i++)
            {
                var item_div = document.createElement("div");
                var content  = "<p>"+jsn[i].name+"</p><ul><li>"+jsn[i].address+
                    "</li><li>"+jsn[i].total_money+" points"+"</li></ul>";
                item_div.setAttribute("Class", "item_div_class");
                item_div.innerHTML = content;
                info_div.appendChild(item_div);
            }
        }
    }
}

/*   $(function(){
    alert("jquery run!");
});
*/

$(document).ready(function(){
    $("#log_out_btn").click(log_out);
});

