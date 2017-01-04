/*
* @Author: ritesh
* @Date:   2015-12-01 14:59:30
* @Last Modified by:   Ritesh Pradhan
* @Last Modified time: 2016-07-19 16:41:33
*/

// var mydata = [
//                { id: "1", invdate: "2007-10-01", name: "test", note: "note", amount: "200.00", tax: "10.00", total: "210.00" },
//                { id: "2", invdate: "2007-10-02", name: "test2", note: "note2", amount: "300.00", tax: "20.00", total: "320.00" },
//                { id: "3", invdate: "2007-09-01", name: "test3", note: "note3", amount: "400.00", tax: "30.00", total: "430.00" },
//                { id: "4", invdate: "2007-10-04", name: "test", note: "note", amount: "200.00", tax: "10.00", total: "210.00" },
//                { id: "5", invdate: "2007-10-05", name: "test2", note: "note2", amount: "300.00", tax: "20.00", total: "320.00" },
//                { id: "6", invdate: "2007-09-06", name: "test3", note: "note3", amount: "400.00", tax: "30.00", total: "430.00" },
//                { id: "7", invdate: "2007-10-04", name: "test", note: "note", amount: "200.00", tax: "10.00", total: "210.00" },
//                { id: "8", invdate: "2007-10-03", name: "test2", note: "note2", amount: "300.00", tax: "20.00", total: "320.00" },
//                { id: "9", invdate: "2007-09-01", name: "test3", note: "note3", amount: "400.00", tax: "30.00", total: "430.00" }
//         ];


$( document ).ready(function() {
 	if (window.location.pathname === "/")
 	{
 		var filter;
    $('#datatable').DataTable({
      'data': mydata,
      'columns': [
        { 'data': 'daac' },
        { 'data': 'dataset_id' },
        { 'data': 'unique_name' }
      ]
    });

    $(document).on('click', '#datatable > tbody > tr', function() {
      event.preventDefault();
      var $td = $($('td', this)[2]);
      var collection_name = $td.text();
      window.location.href = window.location + "_show_keyword_map/" + collection_name;
    });
 	}

  var content = ['<li><strong style="color:red"> Red Text </strong> : No data found. </li>',
                 '<li> <strong style="color:green"> Green Text </strong> : Keywords mapped from this dataset.</li>'].join('');
  $('#popover').popover({
    content: content,
    html: true
  });

	$(document).on("click", '[id^=kvaddButton]' , function() {
  	var id = event.target.id;
		var num = id.split("-", 2)[1]
		var count = $('#kvk-'+num+ ' li').length + 1;
		while ($("#kvk-innerlist-"+num+"-"+count).length != 0) { count += 1;}
		var selectedVal = $('#kvk-'+num +' select').val();
		var newID = 'kvk-innerlist-'+num+'-'+count;
		var removeButtonHtml = '<input type="button" id="kvremoveButton-'+num+'-'+count+'" value="x" class="btn btn-danger btn-xs" />';
		var appendLi = '<a class="list-group-item" id="'+newID+'">'+selectedVal+count+removeButtonHtml+'</a>';
		$('#kvk-'+num).append(appendLi);
   	});

	$(document).on("click", '[id^=vkaddButtonEdit]' , function() {
  	// $(this).parent().remove();
  	var id = event.target.id;
  	var id = id.replace(/->/g, '=>');
		var num = id.split("-", 2)[1]

		var keyword = id.split("-", 3)[2]
		var keyword = keyword.replace(/=>/g, '->');
		// $('#kvkEdit-'+num).append('<li>'+id+'</li>')

		var count = $('#vkv-'+num+ ' li').length + 1;
		while ($("#vkv-innerlistEdit-"+num+"-"+count).length != 0) { count += 1;}
		var newID = 'vkv-innerlistEdit-'+num+'-'+count;
		var nameAttr = 'vkvEdit-' + num + '-' + keyword;
		$('div#select-option-'+num+' select#just_list_of_variables').attr('name', nameAttr);
		var selectOption = $('div#select-option-'+num).html();
		console.log(selectOption);
		// $selectOption.attr('style', 'visilibility:visible');
		var removeButtonHtml = '<input type="button" id="vkremoveButtonEdit-'+num+'-'+count+'" value="x" class="btn btn-danger btn-xs" />';
		var appendLi = '<a class="list-group-item" id="'+newID+'">'+selectOption+' '+removeButtonHtml+'</a>';
		$('#vkvEdit-'+num).append(appendLi);
   	});

	$(document).on("click", '[id^=kvaddButtonEdit]' , function() {
  	// $(this).parent().remove();
  	var id = event.target.id;
  	var id = id.replace(/->/g, '=>');
		var num = id.split("-", 2)[1]

		var keyword = id.split("-", 3)[2]
		var keyword = keyword.replace(/=>/g, '->');
		// $('#kvkEdit-'+num).append('<li>'+id+'</li>')

		var count = $('#kvk-'+num+ ' li').length + 1;
		while ($("#kvk-innerlistEdit-"+num+"-"+count).length != 0) { count += 1;}
		var newID = 'kvk-innerlistEdit-'+num+'-'+count;
		var nameAttr = 'kvkEdit-' + num + '-' + keyword;
		$('div#select-option-'+num+' select#just_list_of_variables').attr('name', nameAttr);
		var selectOption = $('div#select-option-'+num).html();
		console.log(selectOption);
		// // $selectOption.attr('style', 'visilibility:visible');
		var removeButtonHtml = '<input type="button" id="kvremoveButtonEdit-'+num+'-'+count+'" value="x" class="btn btn-danger btn-xs" />';
		var appendLi = '<a class="list-group-item" id="'+newID+'">'+selectOption+' '+removeButtonHtml+'</a>';
		$('#kvkEdit-'+num).append(appendLi);
   	});

	$(document).on("click", '[id^=kvremoveButton]' , function() {
  	var id = event.target.id;
		var [button, num, inum] = id.split("-", 3)
    	$('#kvk-innerlist-'+num+'-'+inum).remove();
  });

 	$(document).on("click", '[id^=kvremoveButtonEdit]' , function() {
  	var id = event.target.id;
	  var [button, num, inum] = id.split("-", 3)
  	$('#kvk-innerlistEdit-'+num+'-'+inum).remove();
 	});

 	$(document).on("click", '[id^=vkremoveButtonEdit]' , function() {
  	var id = event.target.id;
	  var [button, num, inum] = id.split("-", 3)
  	$('#vkv-innerlistEdit-'+num+'-'+inum).remove();
 	});

	$(document).on("click", '[id^=vkaddButton]' , function() {
  	var id = event.target.id;
		var num = id.split("-", 2)[1]
		var count = $('#vkv-'+num+ ' li').length + 1;
		while ($("#vkv-innerlist-"+num+"-"+count).length != 0) { count += 1;}
		var selectedVal = $('#vkv-'+num +' select').val();
		var newID = 'vkv-innerlist-'+num+'-'+count;
		var removeButtonHtml = '<input type="button" id="vkremoveButton-'+num+'-'+count+'" value="x" class="btn btn-danger btn-xs"/>';
		var appendLi = '<a class="list-group-item" id="'+newID+'">'+selectedVal+count+removeButtonHtml+'</a>';
		$('#vkv-'+num).append(appendLi);
 	});

 	$(document).on("click", '[id^=vkremoveButton]' , function() {
  	var id = event.target.id;
	  var [button, num, inum] = id.split("-", 3)
  	$('#vkv-innerlist-'+num+'-'+inum).remove();
 	});


 	// New cfu and cfk edits ---------------------
 	$(document).on("click", '[id^=cfuremoveButtonEdit]' , function() {
  	var id = event.target.id;
	  var [button, num, inum] = id.split("-", 3)
  	$('#cfu-innerlistEdit-'+num+'-'+inum).remove();
 	});

 	$(document).on("click", '[id^=cfkremoveButtonEdit]' , function() {
  	var id = event.target.id;
	  var [button, num, inum] = id.split("-", 3)
  	$('#cfk-innerlistEdit-'+num+'-'+inum).remove();
 	});

	// Onclick li of ul
	$('#keyword-list').on('click', 'li', function(event) {
		event.preventDefault();
		/* Act on the event */
		$('ul > li').removeClass('active');
		$(this).addClass('active');
		var korv = $(this).text();
		alert("Activating ...  " + korv); // gets text contents of clicked li

		//get request from jquery
		$(function() {
			$.getJSON('/_show_it', {
      	korv: korv,
      	is_keyword: 1
     		}, function(data) {
      		$('#mapping #mapping-results').text(data.result);
			});
		});


	});

	// Onclick li of ul
	$('#variable-list').on('click', 'li', function(event) {
		event.preventDefault();
		/* Act on the event */
		$('ul > li').removeClass('active');
		$(this).addClass('active');
		var korv = $(this).text();
		alert("Activating ...  " + korv); // gets text contents of clicked li

		//get request from jquery
		$(function() {
			$.getJSON('/_show_it', {
        	korv: korv,
        	is_keyword: 0
       		}, function(data) {
        		$('#mapping #mapping-results').text(data.result);
			});
		});

	$("#map-button").on('click', function(event)
	{
		alert("this is alert from mapperjs");
		$("div#content-to-hide").hide();
    	$("div#loading-gif").show();


    });

	});

});