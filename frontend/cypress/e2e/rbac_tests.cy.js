describe('Role-Based Access Control', () => {
  it('should restrict access to admin pages for non-admin users', () => {
    cy.login('regularUser', 'password123');
    cy.visit('/admin');
    cy.contains('Access denied').should('be.visible');
    cy.url().should('not.include', '/admin');
  });

  it('should allow access to admin pages for admin users', () => {
    cy.login('adminUser', 'adminPassword');
    cy.visit('/admin');
    cy.contains('Admin Dashboard').should('be.visible');
    cy.url().should('include', '/admin');
  });
});

