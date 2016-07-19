/*
* @Author: ritesh
* @Date:   2015-12-01 14:59:30
* @Last Modified by:   Ritesh Pradhan
* @Last Modified time: 2016-07-13 22:58:34
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
	console.log("This is test log for jss");



			var filter;
   //          $("#jqGrid").jqGrid({

   //              url: 'data.json',
   //              mtype: "GET",
   //              datatype: "json",
			// 	colModel: [
     //                {   label : "Order ID",
					// 	//sorttype: 'integer',
					// 	name: 'OrderID',
					// 	key: true,
					// 	width: 75 ,
					// 	colmenu : true,
					// 	searchoptions : {
					// 		searchOperMenu : false,
					// 		sopt : ['eq','gt','lt','ge','le']
					// 	}
					// },
   //                  {
			// 			label: "Customer ID",
   //                      name: 'CustomerID',
   //                      width: 150,
			// 			hidedlg : true,
   //                      // stype defines the search type control - in this case HTML select (dropdownlist)
   //                      stype: "select",
   //                      // searchoptions value - name values pairs for the dropdown - they will appear as options
   //                      searchoptions: {
			// 				value: " :[All];ALFKI:ALFKI;ANATR:ANATR;ANTON:ANTON;AROUT:AROUT;BERGS:BERGS;BLAUS:BLAUS;BLONP:BLONP;BOLID:BOLID;BONAP:BONAP;BOTTM:BOTTM;BSBEV:BSBEV;CACTU:CACTU;CENTC:CENTC;CHOPS:CHOPS;COMMI:COMMI;CONSH:CONSH;DRACD:DRACD;DUMON:DUMON;EASTC:EASTC;ERNSH:ERNSH;FAMIA:FAMIA;FOLIG:FOLIG;FOLKO:FOLKO;FRANK:FRANK;FRANR:FRANR;FRANS:FRANS;FURIB:FURIB;GALED:GALED;GODOS:GODOS;GOURL:GOURL;GREAL:GREAL;GROSR:GROSR;HANAR:HANAR;HILAA:HILAA;HUNGC:HUNGC;HUNGO:HUNGO;ISLAT:ISLAT;KOENE:KOENE;LACOR:LACOR;LAMAI:LAMAI;LAUGB:LAUGB;LAZYK:LAZYK;LEHMS:LEHMS;LETSS:LETSS;LILAS:LILAS;LINOD:LINOD;LONEP:LONEP;MAGAA:MAGAA;MAISD:MAISD;MEREP:MEREP;MORGK:MORGK;NORTS:NORTS;OCEAN:OCEAN;OLDWO:OLDWO;OTTIK:OTTIK;PERIC:PERIC;PICCO:PICCO;PRINI:PRINI;QUEDE:QUEDE;QUEEN:QUEEN;QUICK:QUICK;RANCH:RANCH;RATTC:RATTC;REGGC:REGGC;RICAR:RICAR;RICSU:RICSU;ROMEY:ROMEY;SANTG:SANTG;SAVEA:SAVEA;SEVES:SEVES;SIMOB:SIMOB;SPECD:SPECD;SPLIR:SPLIR;SUPRD:SUPRD;THEBI:THEBI;THECR:THECR;TOMSP:TOMSP;TORTU:TORTU;TRADH:TRADH;TRAIH:TRAIH;VAFFE:VAFFE;VICTE:VICTE;VINET:VINET;WANDK:WANDK;WARTH:WARTH;WELLI:WELLI;WHITC:WHITC;WILMK:WILMK;WOLZA:WOLZA"
			// 			}
   //                  },
   //                  {
			// 			label: "Order Date",
   //                      name: 'OrderDate',
   //                      width: 150,
			// 			sorttype:'date',
			// 			formatter: 'date',
			// 			srcformat: 'Y-m-d',
			// 			stype : 'text',
			// 			newformat: 'n/j/Y',
   //                      searchoptions: {
   //                          // dataInit is the client-side event that fires upon initializing the toolbar search field for a column
   //                          // use it to place a third party control to customize the toolbar
   //                          dataInit: function (element) {
   //                              $(element).datepicker({
   //                                  id: 'orderDate_datePicker',
   //                                  dateFormat: 'm/d/yy',
   //                                  //minDate: new Date(2010, 0, 1),
   //                                  maxDate: new Date(2020, 0, 1),
   //                                  showOn: 'focus'
   //                              });
   //                          }

   //                      }
   //                  },
   //                  {
			// 			label : "Ship Name",
   //                      name: 'ShipName',
   //                      width: 150,
       //                  searchoptions: {
       //                      // dataInit is the client-side event that fires upon initializing the toolbar search field for a column
       //                      // use it to place a third party control to customize the toolbar

       //                      dataInit: function (element) {
       //                          $(element).autocomplete({
       //                              id: 'AutoComplete',
       //                              source: function(request, response){
							// 			this.xhr = $.ajax({
							// 				url: 'http://trirand.com/blog/phpjqgrid/examples/jsonp/autocompletep.php?callback=?&acelem=ShipName',
							// 				data: request,
							// 				dataType: "jsonp",
							// 				success: function( data ) {
							// 					response( data );
							// 				},
							// 				error: function(model, response, options) {
							// 					response([]);
							// 				}
							// 			});
							// 		},
       //                              autoFocus: true
       //                          });
       //                      },

							// sopt : ['cn']
       //                  }
   //                  },
   //                  {
			// 			label: "Freight",
			// 			sorttype: 'number',
			// 			name: 'Freight',
			// 			width: 150,
			// 			sopt : ['eq']
			// 		},
   //              ],
			// 	loadonce: true,
			// 	viewrecords: true,
   //              width: 780,
   //              height: 250,
   //              rowNum: 10,
			// 	colMenu : true,
			// 	shrinkToFit : false,
   //              pager: "#jqGridPager"
   //          });
			// // activate the toolbar searching
			// $('#jqGrid').jqGrid('navGrid',"#jqGridPager", {
   //              search: false, // show search button on the toolbar
   //              add: false,
   //              edit: false,
   //              del: false,
   //              refresh: true
   //          });
			// var timer;
			// $("#search_cells").on("keyup", function() {
			// 	var self = this;
			// 	if(timer) { clearTimeout(timer); }
			// 	timer = setTimeout(function(){
			// 		//timer = null;
			// 		$("#jqGrid").jqGrid('filterInput', self.value);
			// 	},0);
			// });


	$("#jqGrid").jqGrid({
                datatype: "local",
				data: mydata,
                height: 350,
				// width: 90%,
				autowidth: true,
                colModel: [
                    { label: 'DAAC', name: 'daac', width: 75, },

                    { label: 'Dataset Name', name: 'dataset_id', width: 500,},
                    { label: 'Unique Dataset Name', name: 'unique_name', hidden:true, key:true, colmenu : true, formatter:'showlink', formatoptions:{baseLinkUrl:'someurl.php'}},

                ],
                viewrecords: true, // show the current page, data rang and total records on the toolbar
                caption: "Datasets",
                loadonce: true,
                pager: "#jqGridPager"
            });
			// activate the toolbar searching
			$('#jqGrid').jqGrid('navGrid',"#jqGridPager", {
                search: false, // show search button on the toolbar
                add: false,
                edit: false,
                del: false,
                refresh: true
            });
			var timer;
			$("#search_cells").on("keyup", function() {
				var self = this;
				if(timer) { clearTimeout(timer); }
				timer = setTimeout(function(){
					//timer = null;
					$("#jqGrid").jqGrid('filterInput', self.value);
				},0);
			});

	// function getSelectedRow() {
 //            var grid = $("#jqGrid");
 //            var rowKey = grid.jqGrid('getGridParam',"selrow");

 //            if (rowKey)
 //                alert("Selected row primary key is: " + rowKey);
 //            else
 //                alert("No rows are selected");
 //        }

 		$('#jqGrid').on('click', 'tr', function(event) {
		    event.preventDefault();
		    var tr = $(this)[0];
    		var trID = tr.id;
    		// alert("trID=" + trID);
			var currentLocation = window.location;
    		window.location.href = currentLocation + "_show_keyword_map/" + trID;
		});

     //    $("#jqGrid tr").click(function(){
     //    	var tr = $(this)[0];
    	// 	var trID = tr.id;
    	// 	alert("trID=" + trID);
    	// 	// var currentLocation = window.location;
    	// 	// window.location.href = currentLocation + "_show_keyword_map/" + trID;
    	// });

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

	$("#map-button").on('click', function(event)
	{
		alert("this is alert from mapperjs");
		$("div#content-to-hide").hide();
    	$("div#loading-gif").show();


    });

	});

});