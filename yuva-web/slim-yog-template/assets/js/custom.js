/*----------

Theme Name: Slim Yog - Responsive HTML5 Template
Theme Version: 1.0

----------*/

/*====================
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Loader JS
3.WOW Animation JS
4.Toggle Menu Mobile JS
5.Mobile Menu Toggle Remove JS
6.Scroll To Top JS
7.Smooth Scrolling JS
8.Banner Slider JS
9.Counter Number Count JS
10.Team Slider JS
11.Testimonial Slider JS
12.Sticky Header JS


====================*/

$(document).ready(function() {

    // Whole Script Strict Mode Syntax
    "use strict";

    $(window).ready(function() {
        // Loader JS Start
        $('.loader').fadeOut();
        // Loader JS End
        $('body').removeClass('fixed');
        // Wow Animation JS Start
        new WOW().init();
        // Wow Animation JS Start
    });

    // Toogle Menu Mobile JS Start
    $(".menu-toggle").click(function() {
        $(".main-navigation").toggleClass("toggled");
    });
    // Toogle Menu Mobile JS End

    // Mobile Menu Toggle Remove JS Start
    $(".menu-menu-1-container li a").click(function() {
        $(".main-navigation").removeClass("toggled");
    });
    // Mobile Menu Toggle Remove JS End

    // Scroll To Top JS Start
    $('.scrolltotop').on('click', function() {
        $("html, body").animate({ scrollTop: 0 });
        return false;
    });

    $(".scrolltotop").fadeOut();

    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 100) {
            $(".scrolltotop").fadeIn(300);
        } else {
            $(".scrolltotop").fadeOut(300);
        }
    });
    // Scroll To Top JS End

    // // Smooth Scrolling JS Start
    if (window.location.hash) {
        // smooth scroll to the anchor id
        $('html,body').animate({
            scrollTop: $(window.location.hash).offset().top - 100
        }, 1000, 'swing');
    } else {
        setTimeout(function() { scroll(0, 0); }, 1);
    }

    jQuery('.nav-menu li a').on('click', function(evt) {

        evt.preventDefault();
        var url = $(this).attr('href');
        var id = url.substring(url.lastIndexOf('#'));
        if ($(id).length > 0) {
            $('html, body').animate({
                scrollTop: $(id).offset().top - 100
            }, 10);
        } else {
            window.location.href = url;
        }
    });
    // Smooth Scrolling JS End


    // Banner Slider JS Start
    $('.banner-slider').slick({
        autoplay: true,
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: '<button class="slide-arrow prev-arrow"><i class="fas fa-chevron-left"></i></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><i class="fas fa-chevron-right"></i></button>',
        cssEase: 'cubic-bezier(0.7, 0, 0.3, 1)',
        speed: 900,
        autoplayspeed: 10000,
        lazyLoad: "progressive",
        fade: true,
        responsive: [{
            breakpoint: 992,
            settings: {
                arrows: false,
            }
        }]
    });
    // Banner Slider JS End

    // Counter Number Count JS Start
    var a = 0;
    $(window).scroll(function() {

        var oTop = $('#counter').offset().top - window.innerHeight;
        if (a == 0 && $(window).scrollTop() > oTop) {
            $('.counter-value').each(function() {
                var $this = $(this),
                    countTo = $this.attr('data-count');
                $({
                    countNum: $this.text()
                }).animate({
                        countNum: countTo
                    },

                    {

                        duration: 2000,
                        easing: 'swing',
                        step: function() {
                            $this.text(Math.floor(this.countNum));
                        },
                        complete: function() {
                            $this.text(this.countNum);
                            //alert('finished');
                        }

                    });
            });
            a = 1;
        }

    });
    // Counter Number Count JS End

    // Team Slider JS Start
    $('.team-slider-wp').slick({
        autoplay: true,
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: true,
        prevArrow: '<button class="slide-arrow prev-arrow"><i class="fas fa-chevron-left"></i></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><i class="fas fa-chevron-right"></i></button>',
        responsive: [{
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    dots: false
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    dots: false
                }
            }
        ]
    });
    // Team Slider JS End

    // Testimonial Slider JS Start
    $('.testimonial-slider-wp').slick({
        autoplay: true,
        dots: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: true,
        prevArrow: '<button class="slide-arrow prev-arrow"><i class="fas fa-chevron-left"></i></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><i class="fas fa-chevron-right"></i></button>',
        responsive: [{
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2,
                    dots: false
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    dots: false
                }
            }
        ]
    });
    // Testimonial Slider JS End

});

// Sticky Header
$(window).scroll(function() {
    if ($(window).scrollTop() >= 100) {
        $('.site-header').addClass('sticky-head');
    } else {
        $('.site-header').removeClass('sticky-head');
    }
});