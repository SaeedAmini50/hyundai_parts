
/*=========================================================
	--->  pop up
===========================================================*/

document.addEventListener("DOMContentLoaded", function() {
	var popup = document.getElementById("popup");
	var closeBtn = document.querySelector(".close-btn");
	var okBtn = document.getElementById("okBtn");
	
	// بستن پاپ‌آپ وقتی روی دکمه X یا OK کلیک می‌شود
	closeBtn.addEventListener("click", function() {
		popup.style.display = "none";
	});

	okBtn.addEventListener("click", function() {
		popup.style.display = "none";
	});
});
