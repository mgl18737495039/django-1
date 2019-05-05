// JavaScript Document
//日期切换效果
 $(function(){
	 $('.choicetime a').click(function(){
		 var index = $(this).index();
		 $(this).addClass('active').siblings().removeClass('active');
		 $('.J-notice2-con ul').eq(index).show().siblings().hide();
		 });
	 });
//二维码显示
$(function(){
	$('.fc-conp-bg1').mouseover(function(){
		$('.fc-conp-ewm').show(500);
		});
	$('.fc-conp-bg1').mouseleave(function(){
		$('.fc-conp-ewm').hide();
		});
});
//app的显示
$(function(){
	$('.J-add-app span').hover(function(){
		$('.J-add-appimg').stop().slideDown(500);
		},function(){
		$('.J-add-appimg').stop().slideUp(500);
		});
	});
//底部app显示
$(function(){
	$('.fc-conp-bg3').hover(function(){
		$('.fc-conp-appimg').stop().show(500);
		},function(){
		$('.fc-conp-appimg').stop().hide(500);	
			});
	});
//私募基金的切换
$(function(){
	$('.J-smjjc-title li').click(function(){
		var index = $(this).index();
		$(this).addClass('J-active').siblings().removeClass('J-active');
		$('.J-act-con').eq(index).show().siblings().hide();
		});
});
//积分商城
$(function(){
	$('.J-Imc-top-condi ul:first').css('margin-bottom','10px');
	});
	
	
//积分明细切换
$(function(){
	$('.J-Imxcr-top li').on('click',function(){
		var index = $(this).index();
		$(this).addClass('J-Imccrt-select').siblings().removeClass('J-Imccrt-select');
		$('.J-Imxc-wen-r').eq(index).show().siblings().hide();
		});
	});
//向下无缝走动
$(function(){
	var $container = $('.J-Imxcw-div1 ul');
	var pages = $container.height();
	var liHeight = $
	});
//投资管理中的切换
$(function(){
	$('.J-mainv-click dd').on('click',function(){
		var index = $(this).index();
		$(this).addClass('J-mainvlist-current').siblings().removeClass('J-mainvlist-current');
		$('.J-mainvl-wen').eq(index).show().siblings().hide();
		});
	});
//债权转让
$(function(){
	$('.J-ma-zqzrl-wen dl').children('dd:first').css('width','18%');
	})
//充值
$(function(){
	$('.J-matu-toggle').on('click',function( event){
		$('.J-matu-morebank').slideToggle();
		});
});

//侧边栏滑出电话效果
$(function(){
	$('#J-phonepic').mouseenter(function(){
		$('.J-phonenumb').show().addClass('J-addwidth');
		});
	$('#J-phonepic').mouseleave(function(){
		$('.J-phonenumb').hide().removeClass('J-addwidth');
	 });
});
//我要借款切换
$(function(){
	$('.J-jkcc-title li').click(function(){
		var index = $(this).index();
		$(this).addClass('J-jkc-select').siblings().removeClass('J-jkc-select');
		$('.J-jkcc-list').eq(index).show().siblings().hide();
		});
	});
//我要投资项目列表中的切换
$(function(){
	$('.J-liemu span').click(function(){
	$(this).addClass('J-chose').siblings().removeClass('J-chose');
	});
	});
//弹窗
$(
	function jsMothed(){
	$('.big-link').click(function(){
		$('#myModal').show();
		$('.reveal-modal-bg').show();
		});
	$('.close-reveal-modal').click(function(){
		$('#myModal').hide();
		$('.reveal-modal-bg').hide();
		});
	$('.reveal-modal-bg').click(function(){
		$(this).stop().hide();
		$('#myModal').stop().hide();
		});
	}
	
 );

	