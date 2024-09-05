
/*=========================================================
	--->  pop up
===========================================================*/

document.addEventListener("DOMContentLoaded", function() {
	var popup = document.getElementById("popup");
	var closeBtn = document.querySelector(".close-btn");
	var okBtn = document.getElementById("okBtn");
	var message = "{{ messages|safe }}";

	// اگر پیام وجود داشت، نمایش داده شود
	if (message) {
		document.getElementById("popup-message").innerHTML = message;
		popup.style.display = "flex";
	}

	// بستن پاپ‌آپ وقتی روی دکمه X یا OK کلیک می‌شود
	closeBtn.addEventListener("click", function() {
		popup.style.display = "none";
	});

	okBtn.addEventListener("click", function() {
		popup.style.display = "none";
	});
});
