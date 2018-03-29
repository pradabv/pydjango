$(document).ready(function() {

  $('.data_table').DataTable();

  $('.custom_data_table').DataTable( {
    "footerCallback": function ( row, data, start, end, display ) {
        var api = this.api(), data;

        // Remove the formatting to get integer data for summation
        var intVal = function ( i ) {
            return typeof i === 'string' ?
                i.replace(/[\$,]/g, '')*1 :
                typeof i === 'number' ?
                    i : 0;
        };
        
        col_length = api.columns().header().length;
        for(var col_index=0; col_index<col_length; col_index++){
          if($(api.columns( col_index ).header()).hasClass('show-sum')){
              
              // Total over all pages
              total = api
              .column(col_index)
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );

              // Total over this page
              pageTotal = api
              .column( col_index, { page: 'current'} )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );

              // Update footer
              /*
              $( api.column( col_index ).footer() ).html(
                '$'+pageTotal +' ( $'+ total +' total)'
              );
              */
             $( api.column( col_index ).footer() ).html(pageTotal);


          }

        }
      
       
    }
} );
 
  $startDatePicker = $('.datepicker.start_datepicker');
  $endDatePicker = $('.datepicker.end_datepicker');
  



  
  $startDatePicker.datepicker({
      format:'yyyy-mm-dd',
      autoclose: true,
    }).on('changeDate', function (selected) {
        var minDate = new Date(selected.date.valueOf());
        $endDatePicker.datepicker('setStartDate', minDate);
        
        var date = minDate, y = date.getFullYear(), m = date.getMonth();
        //var firstDay = new Date(y, m, 1);
        var lastDay = new Date(y, m + 1, 0);
        $endDatePicker.datepicker("setDate", lastDay);
    });

  $endDatePicker.datepicker({
    format:'yyyy-mm-dd',
    autoclose: true,
  }).on('changeDate', function (selected) {
          //var maxDate = new Date(selected.date.valueOf());
         // $startDatePicker.datepicker('setEndDate', maxDate);
      });

  
     


  var $input = $(".typeahead");
  /*
  
  $input.typeahead({
    autoSelect: true,
    displayText: function(data){
     return data.tenant_name
    }
  });
  
 function callfun(data){
    $input.data('typeahead').source = data;
 }
  
  $input.keyup(function() {
      var query = $(this).val();
      $.get("rent/ajax/get_country_list", function(data, status){
      $input.data('typeahead').source = data;
    });
  });
  

  $input.change(function() {

    console.log('value changing ')
    var current = $input.typeahead("getActive");
    if (current) {
      // Some item from your model is active!
      if (current.name == $input.val()) {
        // This means the exact match is found. Use toLowerCase() if you want case insensitive match.
      } else {
        // This means it is only a partial match, you can either add a new item
        // or take the active if you don't want new items
      }
    } else {
      // Nothing is active so it is a new value (or maybe empty value)
    }
  });*/

} );
/*
 source: function(query) {
      return $.get("rent/ajax/get_country_list");
    },
    */