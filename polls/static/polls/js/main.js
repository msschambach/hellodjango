(function ($) {
  $(document).ready(function () {

    var choices = $('.choice').map(function () {
      var votes = $(this).children('.votes').first().data().votes;
      return parseInt(votes);
    }).toArray();

    var total_votes = choices.reduce(function (a,b) {
      return a + b;
    });

    $('.choice').each(function (index) {
      var votes = $(this).children('.votes').first().data().votes;
      var percentage_vote = Math.floor((votes/total_votes) * 100);
      $(this)
        .children('.votes')
        .first().children('.progress-bar').first()
        .html(percentage_vote +'%')
        .css({
          width:percentage_vote+"%"
        });

    });

  });
})(jQuery);
