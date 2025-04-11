from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    other_subject = request.form.get('others')
    contact_methods = request.form.getlist('contact_method')
    agreement = request.form.get('agreement')

    errors = []

    if not name or not email or not phone or not message:
        errors.append("All fields are required.")
    if not phone.isdigit():
        errors.append("Phone number must be numeric.")
    if not agreement:
        errors.append("You should agree to our terms and conditions.")

    if subject == "Other":
        subject = other_subject if other_subject else "Other"

    if errors:
        return render_template("contact_form.html", errors=errors)

    return render_template('confirmation.html',
                            name=name,
                            email=email,
                            phone=phone,
                            message=message,
                           subject=subject,
                           contact_methods=contact_methods,
                           agreement='Yes' if agreement else 'No')

if __name__ == '__main__':
    app.run(debug=True)