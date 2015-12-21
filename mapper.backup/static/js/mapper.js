/*
* @Author: ritesh
* @Date:   2015-12-01 14:59:30
* @Last Modified by:   ritesh
* @Last Modified time: 2015-12-21 11:03:39
*/


$( document ).ready(function() {
	console.log("This is test log for js");

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