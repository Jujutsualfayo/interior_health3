describe('Logout Functionality', () => {
  beforeEach(() => {
    cy.login('validUser', 'validPassword');
    cy.visit('/dashboard');
  });

  it('should log out and redirect to the login page', () => {
    cy.get('button.logout').click();
    cy.url().should('include', '/login');
    cy.contains('You have been logged out').should('be.visible');
  });
});

