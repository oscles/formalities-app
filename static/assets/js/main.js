(function (b) {
	b(window);
	var f = b(document), g = b("body");
	b(function () {
		// decorate on the cards initial home
		b("[data-bg-img]").css(
			"background-image",
			function () {
				return 'url("' + b(this).data("bg-img") + '")'
			}).addClass("bg--img").removeAttr("data-bg-img");

		var a = b('[data-toggle="tooltip"]');
		a.length && a.tooltip();
		a = b('[data-trigger="selectmenu"]');
		a.length && a.select2();
		f.on("change", 'input[type="file"]', function (c) {
			c.$el = b(this);
			c.$txt = 0 === c.target.files.length ? "Choose File" : c.target.files[0].name;
			c.$el.hasClass("custom-file-input") && c.$el.next("span").text(c.$txt)
		});

		a = b('[data-trigger="scrollbar"]');
		a.each(function () {
			var c = new PerfectScrollbar(this);
			var a = localStorage.getItem("ps." + this.classList[0]);
			null !== a && (c.element.scrollTop = a)
		});

		a.on("ps-scroll-y", function () {
			localStorage.setItem(
				"ps." + this.classList[0],
				this.scrollTop)
		});

		a = b('[data-trigger="range-slider"]');
		a.length && a.ionRangeSlider();
		b('[data-trigger="sparkline"]').each(function () {
			var a = b(this);
			a.sparkline("html", {
				type: a.data("type"),
				barColor: a.data("color"),
				barWidth: a.data("width"),
				height: a.data("height"),
				values: a.data("value")
			})
		});

		a = b(".records--list");
		// config datatable
		const e = $("#recordsListView").DataTable({
			responsive: !0,
			searching: true,
			language: {
				lengthMenu: "Lista _MENU_ guardados",
				info: "Mostrando de _START_ a _END_ de _TOTAL_",
				infoFiltered: " - filtrados de _MAX_ encontrados"
			},
			dom: '<"topbar"<"toolbar"><"right"li>><"table-responsive"t>p',
			order: [],
			columnDefs: [{targets: "not-sortable", orderable: !1}]
		});

		$('#search').on('keyup', function () {
			e.search(this.value).draw();
		});

		//config menu
		a = b(".sidebar--nav");
		b.each(a.find("li"), function () {
			var a = b(this);
			a.children("a").length && a.children("ul").length && a.addClass("is-dropdown")
		});
		a.on("click", ".is-dropdown > a", function (a) {
			a.preventDefault();
			var c = b(this);
			a = c.siblings("ul");
			c = c.parent();
			var d = c.siblings(".open");
			c.parent()
			.parent(".sidebar--nav").length ?
				(a.slideToggle(), c.toggleClass("open")) :
				(a.add(d.children("ul")).slideToggle(),
					c.add(d).toggleClass("open"))
		});
		b('[data-toggle="sidebar"]').on("click", function (a) {
			a.preventDefault();
			g.toggleClass("sidebar-mini")
		});
		b(".todo--panel").on("submit", "form", function (a) {
			a.preventDefault();
			a = b(this);
			var c = a.find(".form-control");
			b(`
				<li class="list-group-item" style="display: none;">
				<label class="todo--label">
				<input type="checkbox" name="" value="1" class="todo--input">
				<span class="todo--text">${c.val()}</span>
				</label><a href="#" class="todo--remove">&times;</a>
				</li>`).appendTo(a.children(".list-group")).slideDown("slow");
			c.val("")
		}).on("click", ".todo--remove", function (a) {
			a.preventDefault();
			var c = b(this).parent("li");
			c.slideUp("slow", function () {c.remove()})
		})
	})
})(jQuery);




