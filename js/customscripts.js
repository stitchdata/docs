
$('#mysidebar').height($(".nav").height());


$( document ).ready(function() {

    //this script says, if the height of the viewport is greater than 800px, then insert affix class, which makes the nav bar float in a fixed
    // position as your scroll. if you have a lot of nav items, this height may not work for you.
    // var h = $(window).height();
    // //console.log (h);
    // if (h > 800) {
    //     $( "#mysidebar" ).attr("class", "nav affix");
    // }
    // activate tooltips. although this is a bootstrap js function, it must be activated this way in your theme.
    $('[data-toggle="tooltip"]').tooltip({
        placement : 'top'
    });

    /**
     * AnchorJS
     */
    anchors.add('h2,h3,h4,h5');

//***MOBILE Menu view//***MOBILE Menu view//***MOBILE Menu view
$(document).mouseup(function(e)
{
    var container = $(".sidebar-column");

    // if the target of the click isn't the container nor a descendant of the container
    if (!container.is(e.target) && container.has(e.target).length === 0)
    {
        container.removeClass("sidebar-column-show");
    }
});
    $('.mobile-nav-icon').click( function() {
      $(".nav-right").toggleClass("mobile-show");
      $(".nav-right").toggleClass("show");
      $('.mobile-close-out').removeClass("hide");
      $(".mobile-nav-icon").addClass("hide");
  } );
  });

    $('.mobile-close-out').click( function() {
      $(".nav-right").toggleClass("mobile-show");
      $(".nav-right").toggleClass("show");
      $(".mobile-nav-icon").addClass("show");
      $(".mobile-close-out").addClass("hide");
  } );

  $('.sidebar-button').click( function() {
    $(".sidebar-column").toggleClass("sidebar-column-show");
  } );


  //***END MOBILE Menu view//***END MOBILE Menu view//***END MOBILE Menu view



// needed for nav tabs on pages. See Formatting > Nav tabs for more details.
// script from http://stackoverflow.com/questions/10523433/how-do-i-keep-the-current-tab-active-with-twitter-bootstrap-after-a-page-reload
$(function() {
    var json, tabsState;
    $('a[data-toggle="pill"], a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
        var href, json, parentId, tabsState;

        tabsState = localStorage.getItem("tabs-state");
        json = JSON.parse(tabsState || "{}");
        parentId = $(e.target).parents("ul.nav.nav-pills, ul.nav.nav-tabs").attr("id");
        href = $(e.target).attr('href');
        json[parentId] = href;

        return localStorage.setItem("tabs-state", JSON.stringify(json));
    });

    tabsState = localStorage.getItem("tabs-state");
    json = JSON.parse(tabsState || "{}");

    $.each(json, function(containerId, href) {
        return $("#" + containerId + " a[href=" + href + "]").tab('show');
    });

    $("ul.nav.nav-pills, ul.nav.nav-tabs").each(function() {
        var $this = $(this);
        if (!json[$this.attr("id")]) {
            return $this.find("a[data-toggle=tab]:first, a[data-toggle=pill]:first").tab("show");
        }
    });
});


// statuspage
var sp = new StatusPage.page({ page: 'vkh74xvly3rk'});

sp.summary({
  success: function(data) {
    // adds the text description to the dropdown
    $('.color-description').text(data.status.description);
    // appends the status indicator as a class name so we can use the right color for the status light thing
    $('.color-dot').addClass(data.status.indicator);
  }
});
