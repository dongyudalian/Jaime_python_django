function showOther(str)
{
    $.ajax({
        url:"/other_favorite_ajax/",
        type:"GET",
        data:{
          "var1": str
        },
        success:function(str){
            $("#txtHint").html(str)
        }
    })
}