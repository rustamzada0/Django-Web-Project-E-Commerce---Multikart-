from django.test import TestCase

# Create your tests here.

                                                {% for item in items %}
                                                    <div class="col-xl-3 col-6 col-grid-box">
                                                        <div class="product-box">
                                                            <div class="img-wrapper">
                                                                <div class="lable-block">
                                                                    {% if item.variant.new_status == True %}
                                                                        <span class="lable3">new</span>
                                                                    {% endif %}
                                                                    {% if item.variant.actual_price < item.variant.product.price %}
                                                                        <span class="lable4">on sale</span>
                                                                    {% endif %}   
                                                                </div>
                                                                <div class="front">
                                                                    <a href="/product/{{item.variant.get_absolute_url}}"><img src="{{item.image.url}}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                                                                </div>
                                                                <div class="back">
                                                                    <a href="/product/{{item.variant.get_absolute_url}}"><img src="{{item.image.url}}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
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
                                                                        <h6>{{item.variant.product.title}}</h6>
                                                                    </a>
                                                                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
                                                                        of type and scrambled it to make a type specimen book
                                                                    </p>
                                                                    {% if item.variant.actual_price < item.variant.product.price %}
                                                                        <h4>${{item.variant.actual_price}}
                                                                            <del>${{item.variant.product.price}}</del>
                                                                        </h4>
                                                                    {% else %}
                                                                        <h4>${{item.variant.product.price}}
                                                                        </h4>
                                                                    {% endif %}
                                                                    <ul class="color-variant">
                                                                        <li class="bg-light0"></li>
                                                                        <li class="bg-light1"></li>
                                                                        <li class="bg-light2"></li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                {% endfor %}