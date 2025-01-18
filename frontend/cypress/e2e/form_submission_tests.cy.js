describe('Drug Order Form Submission', () => {
  beforeEach(() => {
    cy.login('validUser', 'validPassword');
    cy.visit('/order-drugs');
  });

  it('should submit the drug order form successfully', () => {
    cy.get('input[name="drugName"]').type('Paracetamol');
    cy.get('input[name="quantity"]').type('2');
    cy.get('button[type="submit"]').click();
    cy.contains('Order placed successfully').should('be.visible');
  });

  it('should show error for invalid input', () => {
    cy.get('input[name="drugName"]').type('');
    cy.get('button[type="submit"]').click();
    cy.contains('Drug name is required').should('be.visible');
  });
});

