

$('.add-to-cart-btn').click(function (e) {
    e.preventDefault();
    console.log("Button Clicked");

    let product_id = $(this).closest('.product-details').find('.prodt_id').val();
    console.log("Product ID:", product_id);

    let token = $('input[name=csrfmiddlewaretoken]').val();
    console.log("CSRF Token:", token);

    $.ajax({
        method: "POST",
        url: "/add_to_cart/",
        data: {
            'product_id': product_id,
            'csrfmiddlewaretoken': token
        },
        success: function (response) {
            console.log("Response:", response);
            location.reload();
            if (response.status === "Product added successfully!") {
                alertify.success(response.status);
            } else {
                alertify.error(response.status);
            }
        },
        error: function (xhr, status, error) {
            console.log("Error:", error);
        }
    });
});



let updateBtns = document.getElementsByClassName('update_cart')
let token = $('input[name=csrfmiddlewaretoken]').val();

for (i = 0; i < updateBtns.length; i++) {
   updateBtns[i].addEventListener('click', function(){
      let productId = this.dataset.product
      let action = this.dataset.action
      console.log('productId', productId, 'action', action)
	  console.log("ok")
      updateQuantity(productId, action);
   })
}

function updateQuantity(productId, action){

   let url = '/update_cart/'

   fetch(url, {
      method: "POST",
      headers: {
         'Content-Type': 'application/json',
         'X-CSRFToken': token,
      },
      body:JSON.stringify({'productId':productId, 'action': action})
   })

   .then((response) => {
      
      return response.json();
      
   })

   .then((data) => {
      console.log('data:', data);
      
 	  location.reload();
      
})  
}