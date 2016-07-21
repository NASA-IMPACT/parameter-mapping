/*
* @Author: Ritesh Pradhan
* @Date:   2016-07-12 12:39:55
* @Last Modified by:   Ritesh Pradhan
* @Last Modified time: 2016-07-21 15:36:56
*/

// 'use strict';

$( document ).ready(function() {
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

        		// this.on("maxfilesexceeded", function(file) {
        		// 	alert("No more files please!");
        		// });

        		this.on("error", function(file, message) {
                	alert(message);
                	if (!file.accepted)  {
                		this.removeFile(file);
                		$( "#map-button" ).hide( "fast" );
                	};
			    });


			    this.on("complete", function (file) {
					// alert("All files have uploaded ");
					// finally show the map-button
					var count = this.files.length;
					if (count == 1){
						$( "#map-button" ).show( "fast" );
					}
			     });

			    this.on("success", function (file) {
			          // alert("File successfully uploaded ");
			          // finally show the map-button
			        // $( "#map-button" ).show( "fast" );
			     });
        	},


        	maxFiles:1,
			uploadMultiple:false,
			// acceptedFiles: "image/png, application/x-netcdf, application/x-hdf;subtype=bag",
			acceptedFiles: ".hdf5, .HDF5, .nc, .nc4",
			// maxThumbnailFilesize: 100,
			// maxFilesize: 100,
			// thumbnailWidth: 150,
	  //       thumbnailHeight: 150,
	  //       createImageThumbnails: true,
			dictDefaultMessage: '<i class=\"glyphicon glyphicon-upload \" style=\"font-size: 2em; color:green\"></i><br> Drag a file here to upload, or click to select one',

			// addRemoveLinks:true,
			dictCancelUpload:"Cancel Upload Link",
			dictCancelUploadConfirmation:"Cancel Upload",
			dictRemoveFile:"Delete",
		}
	);

	// fileDropzone.on('sending', function(file) {
	// 	 // Act on the event
	// 	file.name = "test-name-this-is"
	// });

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

	});

});