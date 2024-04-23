const url = window.location.href;
console.log(url);
const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
console.log(searchForm);
console.log(searchInput);
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
console.log(csrfToken);

const sendSearchData = (movie) => {
  $.ajax({
    type: "GET",
    url: "search/",
    data: {
      csrfmiddlewaretoken: csrfToken,
      movie: movie,
    },
    success: (res) => {
      console.log(res);
    },
    error: (err) => {
      console.log(err);
    },
  });
};

searchInput.addEventListener("keyup", (e) => {
  console.log(e.target.value);
  sendSearchData(e.target.value);
});
