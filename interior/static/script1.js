












function addToCart(productName, price) {
    // Get the button element that was clicked
    var button = event.target;
    
    // Replace the button text with ₹ symbol
    button.innerHTML = "₹";
    
    
    updateCartCount();
}

function updateCartCount() {
    // Update the number of items in the cart
    let cartCount = document.querySelectorAll('.add-to-cart').length;
    document.getElementById('cart-count').textContent = cartCount;
}
