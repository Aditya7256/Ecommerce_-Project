$('.plus').click(function(){
    var id = $ (this).attr("pid").toString();
    console.log(id)

var quantity = parseInt($('#quantity').val()) 
quantity += 1
$('#quantity').val(quantity.toString())

})
      