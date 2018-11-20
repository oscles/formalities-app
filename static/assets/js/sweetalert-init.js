const beforeSend = (xhr, settings) => {
	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			let cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
				let cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
		// Only send the token to relative URLs i.e. locally.
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
};

function actionCommand(options, alert = true) {
	let {path, data, method, msg} = options;
	$.ajax({
		beforeSend,
		url: path,
		method,
		data,
		success: (resp) => {
			return alert ? swal('Operación Exitosa!', msg, 'success') : false
		},
		error: (error) => {
			let listErrors = error.responseJSON;
			if (listErrors) {
				let keys = Object.keys(listErrors);
				keys.forEach(key => {
					let input = document.querySelector(`[name='${key}']`);
					input.nextElementSibling.innerHTML = listErrors[key];
				});
			} else {
				swal('Operación Fallída!', error.statusText, 'error');
			}
		}
	});
}

function getObject(modelNamePlural, slug, callback) {
	$.ajax({
		beforeSend,
		url: `/${modelNamePlural}/listar?slug=${slug}`,
		method: 'get',
		success: resp => callback(resp),
		error: error => swal(
			'Operación Fallída!',
			error.message,
			'error'
		)
	});
	return callback;
}

document.body.addEventListener('click', (evt) => {
	const elementClicked = evt.target;
	let modelName = elementClicked.dataset.modelName || '';
	let modelNamePlural = elementClicked.dataset.modelPlural || '';
	let slug = elementClicked.dataset.slug || '';
	let objectName = slug.split('-').join(' ') || '';
	let options = {};

	if (elementClicked.classList.contains('ver')) {
		options = {
			path: `/api/${modelNamePlural}?visited=True&slug=${slug}`,
			method: 'get',
		};
		actionCommand(options, false);
	} else if (elementClicked.classList.contains('eliminar')) {
		options = {
			path: `/${modelNamePlural}/eliminar/${slug}/`,
			method: 'post',
			msg: `${modelName} ${objectName} ha sido eliminado.`,
		};
		actionCommand(options);
		const div = elementClicked.parentElement.parentElement;
		div.parentElement.parentElement.remove();

	} else if (elementClicked.classList.contains('editar')) {
		getObject(modelNamePlural, slug, data => {
				const form = document.getElementById('modal-form');
				const allInputs = [];
				['input', 'select', 'textarea'].forEach(tag => {
					allInputs.push(...form.getElementsByTagName(tag));
				});

				allInputs.forEach(input => {
					const attr = input.getAttribute('name');
					if (input.type !== 'file' && input.type !== 'hidden')
						input.value = data[attr];
				});

				const sendBtn = document.getElementById('send');
				sendBtn.addEventListener('click', evt => {
					const data = {};
					// agregar la información a enviar...
					allInputs.forEach(input => {
						const attr = input.getAttribute('name');
						if (input.type !== 'file')
							data[attr] = input.value;
					});

					options = {
						path: `/api/${modelNamePlural}/${slug}/`,
						method: 'put',
						data,
						msg: `${modelName} ${objectName} ha sido Actualizado.`,
					};
					actionCommand(options);
				});
			}
		)
	}
});

const validateErrors = Array.from(document.querySelectorAll('.validate-error'));
let isError = validateErrors.some(error => error.innerText.length > 0);
if (isError) {
	const message = `Verifíque los mensajes de validación`;
	swal('Operación Fallída!', message, 'error');
}

const alert = document.querySelector('.alert');
if (alert) {
	setTimeout(() => {
		alert.classList.add('hide-alert');
		alert.remove();
	}, 5000);
}

const successMessage = document.getElementById('success');
if (successMessage)
	swal('Operación Exitosa!', successMessage.dataset.message, 'success');

try {
	const ctx = document.getElementById("total-formalities").getContext('2d');
	const chartFormality = new Chart(
		ctx,
		{
			type: 'bar',
			data: {
				labels: [
					"Ene", "Feb", "Mar",
					"Abr", "May", "Jun",
					"Jul", "Ago", "Sep",
					"Oct", "Nov", "Dic"
				],
				datasets: [{
					label: '# de Trámites',
					data: [12, 19, 3, 5, 2, 3, 25, 12, 8, 12, 35, 20],
					backgroundColor: [
						'rgba(255, 99, 132, 0.2)',
						'rgba(54, 162, 235, 0.2)',
						'rgba(255, 206, 86, 0.2)',
						'rgba(75, 192, 192, 0.2)',
						'rgba(153, 102, 255, 0.2)',
						'rgba(255, 159, 64, 0.2)',
						'rgba(255, 99, 132, 0.2)',
						'rgba(54, 162, 235, 0.2)',
						'rgba(255, 206, 86, 0.2)',
						'rgba(75, 192, 192, 0.2)',
						'rgba(153, 102, 255, 0.2)',
						'rgba(255, 159, 64, 0.2)'
					],
					borderColor: [
						'rgba(255,99,132,1)',
						'rgba(54, 162, 235, 1)',
						'rgba(255, 206, 86, 1)',
						'rgba(75, 192, 192, 1)',
						'rgba(153, 102, 255, 1)',
						'rgba(255, 159, 64, 1)',
						'rgba(255,99,132,1)',
						'rgba(54, 162, 235, 1)',
						'rgba(255, 206, 86, 1)',
						'rgba(75, 192, 192, 1)',
						'rgba(153, 102, 255, 1)',
						'rgba(255, 159, 64, 1)'
					],
					borderWidth: 1
				}]
			},
			options: {
				scales: {
					yAxes: [{
						ticks: {
							beginAtZero: true
						}
					}]
				}
			}
		});
} catch (e) {

}

