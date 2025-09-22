from pyscript import document, display

#variables to be used
# "def compute_average" is a function that is tied to the pyclick button in index.html
# this function relates all the bottom variables and etc together as a unit of some kind?? hard to explain but it ensures that--
# -- once the button it is tied to is clicked, the following below is executed
def compute_average(event):
    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)
    answer = (num1 + num2)/2 #variable that finds average of above

#this one below is how the answer variable is displayed on it its own
# as well as for passing and failing scores
    literalgrading = {True: "~ You Passed!", False: "~ You Failed."}
    message = f"Average: {answer:.2f}\t{literalgrading[answer >= 75]}"

# tried to use: document.getElementById("output1").innerHTML = f"Average: {message}"
# but didn't work, so instead used display and just made an output1 variable in the index.html to relate it here
    display(message, target="output1")