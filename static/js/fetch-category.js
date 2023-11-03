    const categoryFunction = async function(){
    const urlParams = new URLSearchParams(window.location.search);
    const categoryValue = urlParams.get("category");
    const colorValue = urlParams.get("colors");
    const itemsContainer = document.getElementById("itemsContainer");
    
    if (categoryValue || colorValue) {
        let url = `http://127.0.0.1:8000/api/categories/?`;

        if (categoryValue) {
            url += `category=${categoryValue}`;
        }

        if (colorValue) {
            if (categoryValue) {
                url += `&`;
            }
            url += `color=${colorValue}`;
        }

        let data = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        });

        let items = await data.json();

        itemsContainer.innerHTML=""

        for (let item of items) {
            const actualPrice = item.variant.actual_price;
            const productPrice = item.variant.product.price;
            const priceHTML = actualPrice < productPrice
                ? `<h4>${actualPrice}</h4> <del>${productPrice}</del>`
                : `<h4>${productPrice}</h4>`;
            
          
            itemsContainer.innerHTML += `
            <div class="col-xl-3 col-6 col-grid-box">
                <div class="product-box">
                    <div class="img-wrapper">
                        <div class="front">
                            <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                        </div>
                        <div class="back">
                            <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                        </div>
                    <div class="cart-info cart-wrap">
                        <button data-toggle="modal" data-target="#addtocart" title="Add to cart"><i
                                class="ti-shopping-cart"></i></button> <a href="javascript:void(0)" title="Add to Wishlist"><i
                                class="ti-heart" aria-hidden="true"></i></a> <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                                class="ti-search" aria-hidden="true"></i></a> <a href="compare.html" title="Compare"><i
                                class="ti-reload" aria-hidden="true"></i></a>
                    </div>
                </div>
                <div class="product-detail">
                    <div>
                        <div class="rating"><i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
                            <a href="product-page(no-sidebar).html">
                                <h6>${item.variant.product.title_en}</h6>
                            </a>
                            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
                                of type and scrambled it to make a type specimen book
                            </p>
                            ${priceHTML}
                            <ul class="color-variant">
                                <li class="bg-light0"></li>
                                <li class="bg-light1"></li>
                                <li class="bg-light2"></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            `
        }
    }
    else {
        let url = `http://127.0.0.1:8000/api/categories/`;

        let data = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                // "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDY3NTg0LCJpYXQiOjE2OTgwNjM5ODQsImp0aSI6ImZiZjMxYzI0NmI5MzRmOGJhMmDxMTE0ZTQ5MmNiNDAwIiwidXNlcl9pZCI6MX0.Pffk8KBrL7uR0FT6H-_vTOfzEv56JkMsUL5F8QDz_OU"
            }
        });

        let items = await data.json();
        let itemsContainer = document.getElementById("itemsContainer")

        itemsContainer.innerHTML=""

        for (let item of items) {
            const actualPrice = item.variant.actual_price;
            const productPrice = item.variant.product.price;
            const priceHTML = actualPrice < productPrice
                ? `<h4>${actualPrice}</h4> <del>${productPrice}</del>`
                : `<h4>${productPrice}</h4>`;
                
            itemsContainer.innerHTML += `
            <div class="col-xl-3 col-6 col-grid-box">
                <div class="product-box">
                    <div class="img-wrapper">
                        <div class="front">
                            <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                        </div>
                        <div class="back">
                            <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                        </div>
                    <div class="cart-info cart-wrap">
                        <button data-toggle="modal" data-target="#addtocart" title="Add to cart"><i
                                class="ti-shopping-cart"></i></button> <a href="javascript:void(0)" title="Add to Wishlist"><i
                                class="ti-heart" aria-hidden="true"></i></a> <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                                class="ti-search" aria-hidden="true"></i></a> <a href="compare.html" title="Compare"><i
                                class="ti-reload" aria-hidden="true"></i></a>
                    </div>
                </div>
                <div class="product-detail">
                    <div>
                        <div class="rating"><i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
                            <a href="product-page(no-sidebar).html">
                                <h6>${item.variant.product.title_en}</h6>
                            </a>
                            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
                                of type and scrambled it to make a type specimen book
                            </p>
                            ${priceHTML}
                            <ul class="color-variant">
                                <li class="bg-light0"></li>
                                <li class="bg-light1"></li>
                                <li class="bg-light2"></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            `
        }

    }
};

categoryFunction()
         

const colors=document.getElementsByClassName("colors")


for(var i=0;i<colors.length;i++){
    colors[i].addEventListener("click",(e)=>{
        console.log(e.target.dataset.color);
        const urlParams = new URLSearchParams(window.location.search);
        const url = new URL(window.location.href);
        url.searchParams.set('colors', e.target.dataset.color);
        window.history.replaceState(null, null, url);
        categoryFunction()
    })
}


