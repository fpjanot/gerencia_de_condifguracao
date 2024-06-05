document.addEventListener('DOMContentLoaded', () => {
    const productForm = document.getElementById('product-form');
    const productList = document.getElementById('product-list');

    productForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const productName = document.getElementById('product-name').value;
        const productCategory = document.getElementById('product-category').value;
        const productQuantity = document.getElementById('product-quantity').value;
        const productPrice = document.getElementById('product-price').value;

        addProductToList(productName, productCategory, productQuantity, productPrice);

        productForm.reset();
    });

    function addProductToList(name, category, quantity, price) {
        const row = document.createElement('tr');

        row.innerHTML = `
            <td>${name}</td>
            <td>${category}</td>
            <td>${quantity}</td>
            <td>R$ ${parseFloat(price).toFixed(2)}</td>
        `;

        productList.appendChild(row);
    }
});
