/*
* @Author: ritesh
* @Date:   2015-12-01 14:59:30
* @Last Modified by:   ritesh
* @Last Modified time: 2015-12-09 13:38:17
*/


$( document ).ready(function() {
	console.log("This is test log for js");

	// Onclick li of ul
	$('#variable-list').on('click', 'li', function(event) {
		event.preventDefault();
		/* Act on the event */
		$('ul > li').removeClass('active');
		$(this).addClass('active');
		var variable = $(this).text();
		alert("Activating ...  " + variable); // gets text contents of clicked li

		//get request from jquery
		$(function() {
			$.getJSON('/_show_it', {
        	variable: variable
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
			dictDefaultMessage: '<i class=\"glyphicon glyphicon-upload\" style=\"font-size: 2em\"></i> Drag a file here to upload, or click to select one',
			// addRemoveLinks:true,
			dictCancelUpload:"Cancel Upload Link",
			dictCancelUploadConfirmation:"Cancel Upload",
			dictRemoveFile:"Delete",
			error:"Incorrect File Format"
		}
	);
	fileDropzone.on("addedfile", function(file) {
  		// file.previewElement.addEventListener("click", function() { fileDropzone.removeFile(file); });
  		removeButtonText = "<button class=\"btn btn-danger delete data-dz-remove \"><i class=\"glyphicon glyphicon-trash\"></i><span>Delete</span></button>"
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
        });

        // Add the button to the file preview element.
        file.previewElement.appendChild(removeButton);
	});
});