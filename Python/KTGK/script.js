function calculate(operation) {
    var inputA = parseFloat(document.getElementById('inputA').value);
    var inputB = parseFloat(document.getElementById('inputB').value);
    var resultElement = document.getElementById('result');

    if (isNaN(inputA) || isNaN(inputB)) {
        resultElement.innerText = "Please enter valid numbers for both inputs.";
        return;
    }

    var result;
    switch (operation) {
        case 'SUM':
            result = inputA + inputB;
            break;
        case 'SUBTRACT':
            result = inputA - inputB;
            break;
        case 'MULTIPLY':
            result = inputA * inputB;
            break;
        case 'DIVIDE':
            if (inputB === 0) {
                resultElement.innerText = "Cannot divide by zero.";
                return;
            }
            result = inputA / inputB;
            break;
        default:
            resultElement.innerText = "Invalid operation.";
            return;
    }

    resultElement.innerText = "Result: " + result;
}

function resetInputs() {
    document.getElementById('inputA').value = "";
    document.getElementById('inputB').value = "";
    document.getElementById('result').innerText = "";
}