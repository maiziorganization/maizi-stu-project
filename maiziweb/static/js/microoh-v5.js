$(function(){
  $(document).on('click', function() {   
    $('#hotkeyword').slideUp();
    $('#keyword-group').slideUp();
    $('.show-card').removeClass('slideInDown').addClass('hidden');
  });
  
  //弹出框显示后的一些操作
  $('.modal').on({
    'show.bs.modal': function (e) {
      $(this).children('.modal-dialog')
      .css('margin','0 auto')
      .wrap('<div class="wrap-modal-main"></div>')
      .wrap('<div class="wrap-modal-con"></div>');
      $('.wrap-modal-main').css({
        'display': 'table',
        'width': '100%',
        'height': '100%'
      });
      $('.wrap-modal-con').css({
        'display': 'table-cell',
        'width': '100%',
        'vertical-align': 'middle'
      });

    },
    'shown.bs.modal': function (e) {
      $(this).find('.form-control').first().focus();
    }
  });
  
  //登陆
  $('#btnLogin').on('click', function () {
    $('#registerModal').modal('hide');
  });
  $('.show-card').on('click', function (event) {
    event.stopPropagation();
  });
  $('.dt-username').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    $('.show-card').toggleClass('hidden slideInDown');
  });
  $('#login').on('click',function(){
      var username = $("#username_id").val();
      var password = $("#password_id").val();
      var errorMessage = $("#errorMessage").val();
      $.post("my_login", {Action:"post","username": username,"password":password}, function(data){
          if(typeof(data.username) != "undefined"){
              $('#loginModal').modal('hide');
              document.getElementById("userLogin").style.display="none";
              document.getElementById("userCenter").style.display="block";
              document.getElementById("userMsg").style.display="block";
              $("#userCenter").html(data.username);
          }
          else if(data.error!=''){
              errorMessage=data.error;
              $("#errorMessage").html(errorMessage);
          }
      })
  });

  //忘记密码
  $('#btnForgetpsw').on('click', function () {
      $('#loginModal').modal('hide');
  });

  $('#reg_password').on('click', function () {
      var reg = $("#rg_password").val();
      $.post("reg_password", {"reg": reg}, function(data){
              if(typeof(data.username) != "undefined"){
                  alert("验证码已发送");
                  $('#forgetpswModal').modal('hide');
              }
              else if(data!=''){
                  var error_message = data.error;
                  $("#error2").html(error_message);
              }
          })

  });
  //注册
  $('#btnRegister').on('click', function () {
      $('#loginModal').modal('hide');
  });
  //邮箱短信注册
  $('#registerLogin').on('click',function(){

      var name = document.getElementById("register-mobile").className;
      //邮件
      if(name == "tab-pane"){
          var register_email = $("#registerEmail").val();
          var register_email_password = $("#registerEmailPassword").val();
          var register_email_check = $("#registerEmailCheck").val();
          var registerError = $("#registerError").val();
          $.post("register_email", {"email": register_email,"password":register_email_password,"check":register_email_check}, function(data){
              if(typeof(data.username) != "undefined"){
                  $('#loginModal').modal('hide');
                  $('#registerModal').modal('hide');
                  document.getElementById("userLogin").style.display="none";
                  document.getElementById("userCenter").style.display="block";
                  document.getElementById("userMsg").style.display="block";
                  $("#userCenter").html(data.username);
              }
              else if(data!=''){
                  var error_message = data.error;
                  $("#registerError").html(error_message);
              }
          })
      }
      //手机
      else if(name == "tab-pane active"){
          var reg_mob = $("#reg_mob").val();
          var reg_password = $("#phone_password").val();
          var check_phone = $("#check_phone").val();
          var mbl_chk = $("#mbl_chk").val();
          var registerError = $("#registerError").val();
          $.post("register_phone", {"phone": reg_mob,"password":reg_password,"checkPhone":check_phone,"check":mbl_chk}, function(data){
              if(typeof(data.username) != "undefined"){
                  $('#loginModal').modal('hide');
                  $('#registerModal').modal('hide');
                  document.getElementById("userLogin").style.display="none";
                  document.getElementById("userCenter").style.display="block";
                  document.getElementById("userMsg").style.display="block";
                  $("#userCenter").html(data.username);
              }
              else if(data!=''){
                  var error_message = data.error;
                  $("#registerError").html(error_message);
              }
          })
      }
  });



  //创建班级

  //search
  $('#search').on({
    click: function(event) {
        //alert($('#search').val());
      event.stopPropagation();
    },
    focus: function() {
      if($(this).val() == '') {
        $('#hotkeyword').slideDown();
      }
    },
    keyup:function() {
      $('#hotkeyword').slideUp();
        var name = $("#search").val();
        if(name!=''){
            $.get("rkSearch", {"name": name}, function(data){
            if(data.message!=[]){
                var str='';
                for(var i=0 ;i<data.length;i++){
                    str +='<a href="" style="background-color:'+data[i].color+';" >'+data[i].name+'</a>';
                }
                if(str!=''){
                    $("#word a").remove();
                    $("#word").append(str);
                }
            }
        })
        }
      $('#keyword-group').slideDown();
    }
  });

  $('.search-dp').click(function(event) {
    event.stopPropagation();
  });

  $('#hotkeyword a').click(function(event) {
    event.preventDefault();
    $('#search').val($(this).text());
      $('#hotkeyword').slideUp();
        var name = $("#search").val();
        var str='';
        if(name!=''){
            $.get("rkSearch", {"name": name}, function(data){

            if(data.message!=[]){

                for(var i=0 ;i<data.length;i++){
                    str +='<a href="" style="background-color:'+data[i].color+';" >'+data[i].name+'</a>';
                }
                if(str!=''){
                    $("#word a").remove();
                    $("#word").append(str);
                }
            }
            })
        }
    $('#hotkeyword').slideUp();
    $('#keyword-group').slideDown();
  });


  //点击收藏
  $('.house').on('click', function (event) {
    event.preventDefault();
    var _thisI = $(this).children('i');
    var _thisIclass = _thisI.hasClass('v5-icon-saved');
    _thisI.toggleClass('v5-icon-saved');
    var _text = (_thisIclass == true) ? '收藏' : '已收藏';
    $(this).children('span').text(_text);
  });
  
  $('.plan-tip').hover(function() {
    $('.plan-tip-box').addClass('show');
  }, function() {
    $('.plan-tip-box').removeClass('show');
  });
  
  $('.feedback-switch').click(function(){
    $(this).toggleClass('active');
    var _has_active = $(this).hasClass('active');
    if(_has_active){
      $(this).parent('.feedback').animate({
        bottom:0
      },500);
    }
    else{
      $(this).parent('.feedback').animate({
        bottom:'-300px'
      },500);
    }
  });
  
  $('img#viptips').hover(function(){
    $(this).tooltip({
      template: '<div class="tooltip tooltip-vip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
    });
    $(this).tooltip('show');
  },function(){
    $(this).tooltip('hide');
  });
  
  $('[data-toggle="tooltip"]').hover(function(){
    $(this).tooltip('show');
  },function(){
    $(this).tooltip('hide');
  });
  
  $('.class-list li').click(function(){
    event.preventDefault();
    $(this).toggleClass('active');
    if($(this).hasClass('active')){
      $(this).siblings().removeClass('active');
      $('#btn-okpay').removeClass('btn-micv5-disabled1').removeAttr('disabled');
    }
    else{
      $('#btn-okpay').addClass('btn-micv5-disabled1').attr('disabled','disabled');
    }
  })
});

function v5_popover_tpl(tpl_class,elem,popover_container,popover_placement,popover_trigger){
  var elem_popover = document.getElementById(elem);
  var popover_c = $('.' + popover_container);
  popover_c.popover({
    content:elem_popover,
    container:'body',
    template:'<div class="popover ' + tpl_class + '" role="tooltip"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>',
    placement:popover_placement,
    trigger:popover_trigger,
    html: true
  });
}


    $(function () {
        //大图切换
        var carousel = $("#carousel").featureCarousel({
            topPadding: 0,
            sidePadding: 0,
            smallFeatureOffset: 100,
            trackerSummation: false
        });
        //首页名师切换
        $('#foo').carouFredSel({
            auto: false,
            prev: '#prev',
            next: '#next',
            mousewheel: true,
            items: {
                visible: 4,
                minimum: 1
            },
            scroll: {
                items: 1,
                duration: 1000
            }
        });


        //登录后
        function show_card() {
            var _parent_left = $('.v5-topbar-login').offset().left;
            var _parent_outw = $('.v5-topbar-login').outerWidth();
            var _this_outw = $('.show-card').outerWidth();
            var _this_left = Math.abs(_parent_left - (_this_outw - _parent_outw));
            $('.show-card').css({
                'left': _this_left
            })
        }

        show_card();
        $(window).resize(function () {
            show_card();
        });

        $('.scroll-pane').jScrollPane({
            autoReinitialise: true
        });
    });


