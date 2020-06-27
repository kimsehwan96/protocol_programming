var settings = {
    "url": "https://9eeme9fjb9.execute-api.ap-northeast-2.amazonaws.com/dev/todos",
    "method": "GET",
    "timeout": 0
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
    //const json = response;
    //const obj = JSON.parse(json);
    //console.log(obj[0].text)
    console.log(response[0].text);
    console.log(response.length);
    const idx = response.length;
    for (i = 0; i <= idx; i++){
        document.write("<h1>");
        document.write(response[i].text);
        document.write("</h1>");
    };
  });