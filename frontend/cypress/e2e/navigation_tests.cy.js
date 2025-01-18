describe('Navigation and Dashboard', () => {
  beforeEach(() => {
    cy.login('validUser', 'validPassword'); // Assume a custom command for login
    cy.visit('/dashboard');
  });

  it('should display the dashboard for logged-in users', () => {
    cy.contains('Dashboard').should('be.visible');
    cy.url().should('include', '/dashboard');
  });

  it('should allow navigation to other sections from the dashboard', () => {
    cy.get('a[href="/profile"]').click();
    cy.url().should('include', '/profile');
    cy.contains('User Profile').should('be.visible');
  });
});

