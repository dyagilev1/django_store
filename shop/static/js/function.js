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
                $("#review-res").html("Review addes successfully!")
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