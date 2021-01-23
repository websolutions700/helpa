let questions = document.querySelectorAll('.survey .question');
let curr = 0;
questions[0].style.display = 'flex';

document.querySelector('.survey .survey-controls .button.prev').onclick = ()=> {
	document.querySelector('.survey .survey-controls .button.next').style.display = 'block';
	document.querySelector('.survey input[type=submit]').style.display = 'none';
	questions[curr].style.display = 'none';
	curr -= 2;
	if (curr <= 0) {
		document.querySelector('.survey .survey-controls .button.prev').style.display = 'none';
		curr = 0;
	};
	questions[curr].style.display = 'block';
	questions[curr].querySelector('p').style.display = 'block';
}


document.querySelector('.survey .survey-controls .button.next').onclick = ()=> {
	document.querySelector('.survey .survey-controls .button.prev').style.display = 'block';
	questions[curr].style.display = 'none';
	console.log(curr);
	curr += 2;
	if (curr >= 28) {
		document.querySelector('.survey .survey-controls .button.next').style.display = 'none';
		document.querySelector('.survey input[type=submit]').style.display = 'block';
		curr = 28;
	}
	questions[curr].style.display = 'block';
}
