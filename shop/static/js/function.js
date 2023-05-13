
const monthNames = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];


$("#commentForm").submit(function(e){
    e.preventDefault();

    let dt = new Date();
    let time = dt.getDate() + " " + monthNames[dt.getUTCMonth()] + ", " + dt.getFullYear(); 

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(res){
            console.log("Comment saved to DB");

            if(res.bool == true){
                $("#review-res").html("Відгук додано успішно!")
                $(".hide-comment-form").hide()
                $(".add-review").hide()

                let _html = '<div>'
                    _html += '<h6>' + res.context.user + '<small> - <i>'+ time +'</i></small></h6>'
                    _html +='<div class="text-primary">'

                    for(var i = 1; i <= res.context.rating; i++){
                        _html += '<i class="fas fa-star text-warning">'
                    }
                    
                    _html +='<p>' + res.context.review + '</p>'
                    _html +='</div>'
                    _html +='</div>'
                    $(".comment-list").prepend(_html)

            }

        }
    })

})

 $(document).on("click", ".add-to-wishlist", function(){
    let product_id = $(this).attr("data-product-item")
    let this_val = $(this)

    console.log("Product ID IS", product_id);

    $.ajax({
        url: "/wishlist/add-to-wishlist",
        data: {
            "id": product_id
        },
        dataType: "json",
        beforeSend: function(){
            console.log("Adding to wishlist....")
            
        }, 
        success: function(response){
            this_val.html("YES")
            if (response.bool === true){
                console.log("Added to wishlist");
            }
           
        }
    })
 })

 $(document).on("click", ".delete-wishlist-product", function(){
    let wishlist_id = $(this).attr("data-wishlist-product")
    let this_val = $(this)

    console.log("wishlist id", wishlist_id)

    $.ajax({
        url: "/wishlist/remove-from-wishlist",
        data: {
            "id": wishlist_id
        },
        dataType: "json",
        beforeSend: function(){
            console.log("Deleting product from wishlist...");
        },
        success: function(response){
            $("#wishlist-list").html(response.data)
            console.log("Delete product from wishlist!");

        }
    })
 })
