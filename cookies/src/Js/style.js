$(function() {
	$("#file").change(function() {
		var current_pic = this.files[0];
		preview_picture(current_pic);
	})
})

function preview_picture(pic) {
	var r = new FileReader();
	r.readAsDataURL(pic);
	r.onload = function(e) {
		$("#img").attr("src", this.result).show();
	}
}

