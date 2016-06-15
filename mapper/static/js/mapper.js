/*
* @Author: ritesh
* @Date:   2015-12-01 14:59:30
* @Last Modified by:   Ritesh Pradhan
* @Last Modified time: 2016-06-15 12:35:03
*/


$( document ).ready(function() {
	console.log("This is test log for jss");

	// Onclick li of ul
	// $('#collection-list').on('click', 'li', function(event) {
	// 	event.preventDefault();
	// 	/* Act on the event */
	// 	$('ul > li').removeClass('active');
	// 	$(this).addClass('active');
	// 	var collection_name = $(this).text();
	// 	alert("Activating ...  " + collection_name); // gets text contents of clicked li

	// 	//get request from jquery
	// 	$(function() {
	// 		$.getJSON('/_show_map', {
 //        	collection_name: collection_name,
 //       		}, function(data) {
 //        		$('#mapping #mapping-results').text(data.result);
	// 		});
	// 	});


	// });


	// $('[id^=addButton]').click(function (event) {
	// 	var id = event.target.id;
	// 	var num = id.split("-", 2)[1]
	// 	$('#kvk-'+num).append('<li>'+id+'</li>')
	// 	$('#kvk-'+num).append('<li>'+num+'</li>')
	// 	$('#kvk-'+num).append('<li>'+$('#kvk-'+num+ ' li').length+'</li>')
	// 	var count = $('#kvk-'+num+ ' li').length + 1;
	// 	while ($("#kvk-innerlist-"+num+"-"+count).length != 0) { count += 1;}

	// 	var selectedVal = $('#kvk-'+num +' select').val();
	// 	var newID = 'kvk-innerlist-'+num+'-'+count;
	// 	var removeButtonHtml = '<input type="button" id="removeButton-'+num+'-'+count+'" value="Remove" />';
	// 	var appendLi = '<li class="list-group-item" id="'+newID+'">'+selectedVal+count+removeButtonHtml+'</li>';
	// 	$('#kvk-'+num).append(appendLi).listview('refresh');
	// 	$('#kvk-'+num).append('<li class="list-group-item">'+selectedVal+count+'</li>')

	// });

	// var keyword_header =$('div.list-group-each-keyword').text().trim();
	// console.log(keyword_header);
	// key_arr = keyword_header.split('->');
	// console.log(key_arr.length);
	// $("div.list-group-each-keyword").html("<span>"+key_arr[0] + key_arr[1]+ "</span>" );


	$(document).on("click", '[id^=kvaddButton]' , function() {
    	// $(this).parent().remove();
    	var id = event.target.id;
		var num = id.split("-", 2)[1]
		var count = $('#kvk-'+num+ ' li').length + 1;
		while ($("#kvk-innerlist-"+num+"-"+count).length != 0) { count += 1;}
		var selectedVal = $('#kvk-'+num +' select').val();
		var newID = 'kvk-innerlist-'+num+'-'+count;
		var removeButtonHtml = '<input type="button" id="kvremoveButton-'+num+'-'+count+'" value="Remove" class="btn btn-danger" />';
		var appendLi = '<li class="list-group-item" id="'+newID+'">'+selectedVal+count+removeButtonHtml+'</li>';
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
		var removeButtonHtml = '<input type="button" id="vkremoveButtonEdit-'+num+'-'+count+'" value="Remove" class="btn btn-danger" />';
		var appendLi = '<li class="list-group-item" id="'+newID+'">'+selectOption+' '+removeButtonHtml+'</li>';
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
		var removeButtonHtml = '<input type="button" id="kvremoveButtonEdit-'+num+'-'+count+'" value="Remove" class="btn btn-danger" />';
		var appendLi = '<li class="list-group-item" id="'+newID+'">'+selectOption+' '+removeButtonHtml+'</li>';
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
    	// $(this).parent().remove();
    	console.log("Inside vkaddButton");
    	var id = event.target.id;
		var num = id.split("-", 2)[1]
		var count = $('#vkv-'+num+ ' li').length + 1;
		while ($("#vkv-innerlist-"+num+"-"+count).length != 0) { count += 1;}
		var selectedVal = $('#vkv-'+num +' select').val();
		var newID = 'vkv-innerlist-'+num+'-'+count;
		var removeButtonHtml = '<input type="button" id="vkremoveButton-'+num+'-'+count+'" value="Remove" />';
		var appendLi = '<li class="list-group-item" id="'+newID+'">'+selectedVal+count+removeButtonHtml+'</li>';
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


	});

	// DropZone Effects
	Dropzone.autoDiscover = false;
	var fileDropzone = new Dropzone("#file-dropzone",
		{ /* options */
			init: function()
			{
        		var $this = this;
        		$("#data-dz-remove").click(function()
        		{
            		$this.removeAllFiles(true);
        		});
        	},
			maxFiles:1,
			uploadMultiple:false,
			dictDefaultMessage: '<i class=\"glyphicon glyphicon-upload \" style=\"font-size: 2em; color:green\"></i><br> Drag a file here to upload, or click to select one',
			// addRemoveLinks:true,
			dictCancelUpload:"Cancel Upload Link",
			dictCancelUploadConfirmation:"Cancel Upload",
			dictRemoveFile:"Delete",
			error:"Incorrect File Format"
		}
	);
	fileDropzone.on('sending', function(file) {
		/* Act on the event */
		file.name = "test-name-this-is"
	});

	fileDropzone.on("addedfile", function(file) {
  		// file.previewElement.addEventListener("click", function() { fileDropzone.removeFile(file); });
  		removeButtonText = "<button class=\"btn btn-danger delete data-dz-remove btn-block\" ><i class=\"glyphicon glyphicon-trash\"></i><span>Delete</span></button>"
  		// Create the remove button
        var removeButton = Dropzone.createElement(removeButtonText);


        // Capture the Dropzone instance as closure.
        var _this = this;

        // Listen to the click event
        removeButton.addEventListener("click", function(e) {
          // Make sure the button click doesn't submit the form:
          e.preventDefault();
          e.stopPropagation();

          // Remove the file preview.
          _this.removeFile(file);
          // If you want to the delete the file on the server as well,
          // you can do the AJAX request here.

          //hide the shown map-button
          $( "#map-button" ).hide( "fast" );
        });

        // Add the button to the file preview element.
        file.previewElement.appendChild(removeButton);

        // finally show the map-button
        $( "#map-button" ).show( "fast" );
	});
});