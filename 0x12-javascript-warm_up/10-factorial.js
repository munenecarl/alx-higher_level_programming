#!/usr/bin/node

function recursive_function(num) {
	if (num == 0 || isNaN(num)) {
		return 1;	
	}
	return num * recursive_function(num - 1);	
}

console.log(recursive_function(parseInt(process.argv[2])))
