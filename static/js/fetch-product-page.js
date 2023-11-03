window.addEventListener('load', async function() {
    let productID = document.getElementById("productID").value
    let data = await fetch(`http://127.0.0.1:8000/api/product/${productID}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });
    let product = await data.json();
    let colorContainer = document.getElementById("colorContainer")

    for (let variant of product.variant) {
        console.log(variant);
        colorContainer.innerHTML += `
        <a href="/product/${variant.get_absolute_url}">
        <li style="background-color: ${variant.color};">
        </li>
        </a>
        `
        }
    });