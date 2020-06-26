var settings = {
    "url": "https://9eeme9fjb9.execute-api.ap-northeast-2.amazonaws.com/dev/todos",
    "method": "GET",
    "timeout": 0
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });