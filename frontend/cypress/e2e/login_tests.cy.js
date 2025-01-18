describe('Login Functionality', () => {
  beforeEach(() => {
    cy.visit('/login');
  });

  it('should log in with valid credentials', () => {
    cy.get('input[name="username"]').type('validUser');
    cy.get('input[name="password"]').type('validPassword');
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/dashboard');
    cy.contains('Welcome, validUser');
  });

  it('should not log in with invalid credentials', () => {
    cy.get('input[name="username"]').type('invalidUser');
    cy.get('input[name="password"]').type('invalidPassword');
    cy.get('button[type="submit"]').click();
    cy.contains('Invalid username or password').should('be.visible');
  });

  it('should show validation errors on empty submission', () => {
    cy.get('button[type="submit"]').click();
    cy.contains('Username is required').should('be.visible');
    cy.contains('Password is required').should('be.visible');
  });
});

