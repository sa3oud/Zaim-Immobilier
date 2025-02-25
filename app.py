from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'zaim_immobilier_secret_key'  # Nécessaire pour les messages flash

# Route principale - page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour traiter le formulaire de contact
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        whatsapp = request.form.get('whatsapp')
        interest = request.form.get('property-interest')
        message = request.form.get('message')
        
        # Ici, vous pouvez ajouter la logique pour enregistrer ces données
        # Par exemple : envoyer un email, sauvegarder dans une base de données, etc.
        
        # Pour l'exemple, nous allons simplement afficher un message de succès
        flash(f'Merci {name}, votre message a bien été envoyé!', 'success')
        
        # Redirection vers la page de confirmation
        return render_template('contact_success.html', 
                              name=name, 
                              email=email, 
                              interest=interest)
    
    # Si la méthode n'est pas POST, rediriger vers la page d'accueil
    return redirect(url_for('index'))

# Injecter l'année en cours dans tous les templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

# Démarrage de l'application
if __name__ == '__main__':
    app.run(debug=True)
