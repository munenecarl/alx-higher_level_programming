#!/usr/bin/node

if (process.argv.length <= 3) {
	console.log(0);
} else {
	let biggest_num = Number(process.argv[2]);
	let second_biggest_num = Number(process.argv[3]);

	if (biggest_num < second_biggest_num) {
		[biggest_num, second_biggest_num] = [second_biggest_num, biggest_num];
	}

	for (let index = 4; index < process.argv.length; index++) {
		let current_num = Number(process.argv[index]);
		if (current_num > biggest_num) {
			second_biggest_num = biggest_num;
			biggest_num = current_num;
		} else if (current_num > second_biggest_num) {
			second_biggest_num = current_num;
		}
	}

	console.log(second_biggest_num);
}