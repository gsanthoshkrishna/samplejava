from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Guru!"


 
@app.route("/prime4")
def prime4():
    retVal = is_prime(4)
    if retVal == True:
        return "Hello Guru! value is a prime number"
    return "Hello Guru! value is not a prime number"

@app.route("/prime3")
def prime3():
    retVal = is_prime(3)
    if retVal == True:
        return "Hello Guru! value is prime"
    return "Hello Guru! value is not a prime"



def is_prime(a):
    if a == 3:
        return True
    return False


if __name__ == "__main__":
    app.run()
