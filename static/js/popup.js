

/*=========================================================
	--->  pop up
===========================================================*/



document.addEventListener("DOMContentLoaded", function() {
	var popup = document.getElementById("popup");
	var closeBtn = document.querySelector(".close-btn");
	var okBtn = document.getElementById("okBtn");

	// نمایش پاپ‌آپ هنگام بارگذاری صفحه
	popup.style.display = "flex";

	// بستن پاپ‌آپ وقتی روی دکمه X کلیک می‌شود
	closeBtn.addEventListener("click", function() {
		popup.style.display = "none";
	});

	// بستن پاپ‌آپ وقتی روی دکمه OK کلیک می‌شود
	okBtn.addEventListener("click", function() {
		popup.style.display = "none";
	});
});