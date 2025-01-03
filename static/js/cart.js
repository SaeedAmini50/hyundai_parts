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