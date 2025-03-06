$(document).ready(function () {
  let favicon = "https://fptoj.com/static/icons/icon.svg";

  $("link[rel='icon']").remove();
  
  $("head").append(`<link rel="icon" type="image/svg+xml" href="${favicon}">`);
});
  

$(document).ready(function() {
  $('a.md-header__button.md-logo').attr('href', 'https://fptoj.com/');
  $("details p").each(function() {
      renderMathInElement(this, {
        delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "\\begin{align}", right: "\\end{align}", display: true},   // Block math
          {left: "$", right: "$", display: false},   // Inline math
          {left: "\\[", right: "\\]", display: true}, // Block math kiểu LaTeX
          {left: "\\(", right: "\\)", display: false} // Inline math kiểu LaTeX
        ]
      });
  });
});

$(document).on("toggle", "details", function() {
  $(this).find("p").each(function() {
      console.log("🔄 Mở <details> - Trước khi render:", $(this).html());
      renderMathInElement(this, {
          delimiters: [
              {left: "$$", right: "$$", display: true},
              {left: "\\(", right: "\\)", display: false},
              {left: "$", right: "$", display: false}
          ]
      });
      console.log("✅ Sau khi render lại:", $(this).html());
  });
});