function sortTable(columnIndex) {
    const table = document.getElementById('myTable');
    const tbody = table.tBodies[0]; // Target the tbody
    const rows = Array.from(tbody.rows); // Get all rows as an array
    
    // Get current sort order based on column header
    const th = table.querySelectorAll('th')[columnIndex];
    let isAscending = th.classList.contains('sorted-asc');
    
    // Sort rows based on the selected column
    const sortedRows = rows.sort((a, b) => {
      const aText = a.cells[columnIndex].innerText.toLowerCase();
      const bText = b.cells[columnIndex].innerText.toLowerCase();
      
      return isAscending ? (aText > bText ? 1 : -1) : (aText < bText ? 1 : -1);
    });
  
    // Append sorted rows back to the tbody
    sortedRows.forEach(row => tbody.appendChild(row));
  
    // Toggle the sort order for the next click
    th.classList.toggle('sorted-asc', !isAscending);
    th.classList.toggle('sorted-desc', isAscending);
    
    // Remove sorted classes from other headers
    Array.from(table.querySelectorAll('th')).forEach(header => {
      if (header !== th) {
        header.classList.remove('sorted-asc', 'sorted-desc');
      }
    });
  }
  