/* App JS */

$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip(); 
});

function expenseSearch() {
  var input = document.getElementById("expense-search");
  var query = input.value.toUpperCase();
  var list = document.getElementById("expense-list");
  var expenses = list.getElementsByTagName('li');

  for (i = 0; i < expenses.length; i++) {
    let expense = expenses[i].getElementsByTagName("span")[0];
    let txtValue = expense.textContent;
    if (txtValue.toUpperCase().indexOf(query) > -1) {
      expenses[i].style.display = "";
    } else {
      expenses[i].style.display= "none";
    }
  }
}