// $(function(){
// 	$(document).one('click', '.like-review', function(e) {
// 		$(this).html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
// 		$(this).children('.fa-heart').addClass('animate-like');
// 	});
// });

var buttons = document.getElementById('heart-btn')

Array.prototype.forEach.call(buttons, function(b) {
    b.addEventListner('click', createAni);
})

function createAni(e) {
    document.one('click', '.like-review', function(z) {
        this.html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
        this.children('.fa-heart').addClass('animate-like')
    })
}