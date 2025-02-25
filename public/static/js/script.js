document.addEventListener('DOMContentLoaded', function() {
    // Fonction pour faire défiler jusqu'à la section de contact
    window.scrollToContact = function() {
        const contactSection = document.getElementById('contact-section');
        contactSection.scrollIntoView({ behavior: 'smooth' });
        
        // Mettre en surbrillance le formulaire
        const contactForm = document.getElementById('contact-form');
        contactForm.classList.add('highlight');
        
        // Focus sur le premier champ du formulaire
        document.getElementById('name').focus();
        
        // Pré-remplir le champ de message avec le quartier recherché
        const searchInput = document.querySelector('.search-input');
        const messageField = document.getElementById('message');
        if (searchInput.value.trim() !== '') {
            messageField.value = "Je recherche une propriété à " + searchInput.value;
        }
    };
    
    // Formatage des numéros de téléphone
    const phoneInput = document.getElementById('phone');
    const whatsappInput = document.getElementById('whatsapp');
    
    function formatPhoneNumber(input) {
        if (!input) return;
        
        input.addEventListener('input', function(e) {
            // Supprimer tous les caractères non numériques
            let value = this.value.replace(/\D/g, '');
            
            // S'assurer qu'on commence par +212
            if (!value.startsWith('212')) {
                if (value.startsWith('0')) {
                    value = '212' + value.substring(1);
                } else {
                    value = '212' + value;
                }
            }
            
            // Limiter à la longueur maximale (12 chiffres)
            if (value.length > 12) {
                value = value.substring(0, 12);
            }
            
            // Formater le numéro
            if (value.length >= 3) {
                value = '+' + value.substring(0, 3) + ' ' + value.substring(3, 4);
                
                if (value.length >= 7) {
                    value += ' ' + value.substring(6, 8);
                }
                
                if (value.length >= 10) {
                    value += ' ' + value.substring(9, 11);
                }
                
                if (value.length >= 13) {
                    value += ' ' + value.substring(12, 14);
                }
            }
            
            this.value = value;
        });
    }
    
    formatPhoneNumber(phoneInput);
    formatPhoneNumber(whatsappInput);
    
    // Gestion de la soumission du formulaire
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simuler l'envoi du formulaire (à remplacer par votre logique réelle)
            const submitButton = contactForm.querySelector('.submit-button');
            const originalText = submitButton.textContent;
            
            submitButton.disabled = true;
            submitButton.textContent = 'Envoi en cours...';
            
            // Simulation d'une requête AJAX (à remplacer par votre propre appel API)
            setTimeout(function() {
                // Redirection vers une page de confirmation ou affichage d'un message
                alert('Merci pour votre message ! Nous vous contacterons bientôt.');
                
                // Réinitialiser le formulaire
                contactForm.reset();
                
                // Restaurer le bouton
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }, 1500);
        });
    }
    
    // Animation de défilement doux pour tous les liens internes
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Effet visuel lorsqu'on survole les cartes de propriétés
    const propertyCards = document.querySelectorAll('.property-card');
    propertyCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-8px)';
            card.style.boxShadow = '0 12px 25px rgba(0, 0, 0, 0.12)';
            
            const propertyImage = card.querySelector('.property-image');
            if (propertyImage) {
                propertyImage.style.transform = 'scale(1.05)';
            }
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
            card.style.boxShadow = '';
            
            const propertyImage = card.querySelector('.property-image');
            if (propertyImage) {
                propertyImage.style.transform = '';
            }
        });
    });
});
