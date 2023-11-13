#!/usr/bin/node

if (isNaN(process.argv[2])) {
	console.log("Missing size")
} else {
	for (let index = 0; index < Number(process.argv[2]); index++) {
		let row = '';
		for (let second_index = 0; second_index < Number(process.argv[2]); second_index++) {
			row += 'X';
		}
		console.log(row)
	}
}
