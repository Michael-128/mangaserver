var isVisible = false;
var fillWidth = false;

var file = $("#filename").val()


function adjustImageSize() {
    if(!fillWidth) {
        $("#image").css("height", window.innerHeight)
    }
    else {
        $("#image").css("height", "auto")
    }
}
adjustImageSize()

$(window).on("resize", adjustImageSize)

function showControls() {
    $(".current-page-number").fadeIn(200).css("display", "flex")
    $(".controls").fadeIn(200).css("display", "flex")
    isVisible = true
}

function hideControls() {
    $(".current-page-number").fadeOut(200)
    $(".controls").fadeOut(200)
    isVisible = false
}

function toggleControls() {
    if(!isVisible) {
        showControls()
    } else {
        hideControls()
    }
}

var currentPage = 1
var maxPage = parseInt($("#image").attr("max"))

function changePage() {
    $(".current-page-number").text(currentPage+"/"+maxPage)
    fetch("/get_image?file="+file+"&page="+currentPage)
    .then(res => res.blob())
    .then(res => {
        var url = URL.createObjectURL(res)
        console.log(res, url)
        $("#image").attr('src', url)
    })
    //showCurrentPage()
}

changePage()

$("#image").on("load", function(e) {
    if(fillWidth) window.scrollTo(0,0)
})

function nextPage() {
    currentPage++
    changePage()
    return currentPage
}

function previousPage() {
    currentPage--
    changePage()
    return currentPage
}

$("#next-btn").on("click", function(e) {
    hideControls()

    if(currentPage >= maxPage) return
    nextPage()
})

$("#previous-btn").on("click", function(e) {
    hideControls()

    if(currentPage <= 1) return
    previousPage()
})

$("#controls-btn").on("click", toggleControls)


function iOSversion() {
    if (/iP(hone|od|ad)/.test(navigator.platform)) {
      // supports iOS 2.0 and later: <http://bit.ly/TJjs1V>
      var v = (navigator.appVersion).match(/OS (\d+)_(\d+)_?(\d+)?/);
      return [parseInt(v[1], 10), parseInt(v[2], 10), parseInt(v[3] || 0, 10)];
    }
    return false;
  }


function disableInputs(e) {
    $("#image-scale").prop("disabled", true)
    $("#image-scale-span").text("100%")
    $("#image-scale").val("100")
}

function enableInputs(e) {
    $("#image-scale").prop("disabled", false)
}

function toggleInputs(e) {
    if(!fillWidth) {
        disableInputs()
    } else {
        enableInputs()
    }
}

var btnColor = $("#fill-width-btn").css("color")

$("#fill-width-btn").on("click", function(e) {

    toggleInputs(e)

    if(fillWidth) {
        $("#image").css("height", window.innerHeight)
        $("#image").css("width", "")
        $(e.target).css("color", btnColor)
        fillWidth = false
    } else {

        $("#image").css("height", "auto")

        $("#image").css("width", "100vw")
        $(e.target).css("color", "lightgreen")
        fillWidth = true
    }
})

$("#image-scale").on("input", function(e) {
    $("#image-scale-span").text($(e.target).val()+"%")
    $("#image").css("height", $(e.target).val()+"vh")
})


$("#skip-10").on("click", function(e) {
    if(currentPage+10 > maxPage) {
        currentPage = maxPage
        changePage()
    } else {
        currentPage += 10
        changePage()
    }
})

$("#skip-10-back").on("click", function(e) {
    if(currentPage-10 < 1) {
        currentPage = 1
        changePage()
    } else {
        currentPage -= 10
        changePage()
    }
})