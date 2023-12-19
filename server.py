# Import libraries
from flask import Flask,render_template,redirect,request,url_for
# Instantiate Flask functionality
app=Flask(__name__)

# Sample data
transactions=[
{'id': 1,'name':'Ayush Pandey', 'date':'2023-06-01', 'amount': 100000000},
{'id': 2,'name':'Abhinav Garg', 'date':'2023-07-12', 'amount': 200},
{'id': 3,'name':'Ankur Bist', 'date':'2023-11-02', 'amount': 300},
{'id': 4,'name':'Tej Pratap', 'date':'2022-4-07', 'amount': 400},

]

#Login details
login_details=[
    {'username':'inbox.ayushpandey@gmail.com','password':'iwonttellyou'},
     
]

@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login",methods=["POST"])
def verify_user():
    username=request.form['username']
    password=request.form['password']

    for user in login_details:
   
            if user['username'] == username and user['password'] == password :
                return redirect(url_for("get_transactions"))
    
    return render_template("user_not_found.html")              
        




# Read operation
@app.route("/transactions")
def get_transactions():
    return render_template("transactions.html",transactions=transactions)


# Create operation
@app.route("/add",methods=["GET","POST"])
def add_transaction():
    if request.method=="POST":

        #create the new transaction object
        transaction={
         'id':len(transactions)+1,
         'name':request.form['name'],
         'date':request.form['date'],
         'amount':float(request.form['amount'])
        }
        #append the new transaction to the list os transactions 
        transactions.append(transaction)

        #Redirect to the transactions page
        return redirect(url_for('get_transactions'))
    
    return render_template("form.html")

         
# Update operation
@app.route("/edit/<int:transaction_id>",methods=["GET","POST"])
def edit_transaction(transaction_id):
     if request.method=="POST":
        date=request.form['date']
        amount=request.form['amount']
        name=request.form['name']
        for person in transactions:
            if person['id']==transaction_id:
                person['date']=date
                person['amount']=amount
                person['name']=name
                break

        return redirect(url_for("get_transactions"))

     # Find the transaction with the matching ID and render the edit form
     for transaction in transactions:
        if transaction['id']==transaction_id:
            return render_template("edit.html",transaction=transaction)




# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id']==transaction_id:
            transactions.remove(transaction)
            break

    #redirect to transactions list page
    return redirect(url_for("get_transactions"))  

  
# Run the Flask app
if __name__==  "__main__":
    app.run(debug=True)
