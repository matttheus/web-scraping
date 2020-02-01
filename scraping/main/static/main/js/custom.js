document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
      document.getElementById('search-input').focus();
    }
  }