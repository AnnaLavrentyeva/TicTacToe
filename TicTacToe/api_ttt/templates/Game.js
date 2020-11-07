function StartGame() {
  var that = this;
  var player = '';

  that.input = ko.observable();

  that.cell = ko.observableArray(['0','1','2','3','4','5','6','7','8'])

  that.move = function(n){
        player = n;
        console.log(player)
          for(var i=0; i<2; i++){
          document.getElementsByClassName("but")[i].disabled = true;
        }
  }


  that.td0 = function(n){
  $.ajax({
          type: 'PUT',
          url: '/game',
          data: ko.toJSON({
          value : n,
          x : that.cell()
          }),
      })

      .done(function(result) {
        that.input(null);
          if(result.winner == 'O'){
            alert('O wins');
            location.reload();
          }
          else if (result.winner == 'X'){
            alert('X wins');
            location.reload();
          }
          else if(result.winner == 'Draw'){
            alert('No winner today!');
            location.reload();
          }
          else if(result.wrong_cell == 'true'){
            alert('Choose other number.');
          }
          else{
            that.cell(result.cell);
            console.log(that.cell());
          }
      })

      .fail(function (jqXHR, textStatus, error) {
        console.log("Post error: " + error);
      });

  }


  that.submit = function() {
      $.ajax({
          type: 'PUT',
          url: '/game',
          data: ko.toJSON({
          value : that.input(),
          x : that.cell()
          })
      })

      .done(function(result) {
        that.input(null);
          if(result.winner == 'O'){
            alert('O wins');
            location.reload();
          }
          else if (result.winner == 'X'){
            alert('X wins');
            location.reload();
          }
          else if(result.winner == 'Draw'){
            alert('No winner today!');
            location.reload();
          }
          else if(result.wrong_cell == 'true'){
            alert('Choose other number.');
          }
          else{
            that.cell(result.cell);
            console.log(that.cell());
          }
      })

      .fail(function (jqXHR, textStatus, error) {
        console.log("Post error: " + error);
      });

  }

}

    $(document).ready(function () {
   // document.getElementById("table").style.display = "none";
        console.log("Load")
        ko.applyBindings(new StartGame(), document.getElementById('loader'));
    });



